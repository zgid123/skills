#!/usr/bin/env python3
"""Read-only validation of swe-lifecycle documentation; Python 3.9+, no dependencies."""

import argparse
import datetime
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
DOMAIN = r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*"
NUMBER = r"(?!00000)[0-9]{5}"
SEQUENCE = r"(?!0000)[0-9]{4}"
ID_PATTERN = re.compile(
    rf"(?:REQ-{NUMBER}|CHG-(?:{NUMBER}|(?:{NUMBER}|{DOMAIN})-{SEQUENCE})|ADR-{NUMBER}|KNW-{DOMAIN}|LOG-(?:{NUMBER}|{DOMAIN})-{SEQUENCE})\Z"
)
STATUSES = {
    "REQ": {"draft", "approved", "retired"},
    "CHG": {"draft", "proposed", "approved", "implementing", "implemented", "rejected", "withdrawn"},
    "ADR": {"proposed", "accepted", "superseded", "rejected"},
    "KNW": {"draft", "verified"},
    "LOG": {"draft", "finalized"},
}
# Concise templates are canonical; full prior sets remain valid for existing docs.
SECTIONS = {
    "REQ": {"Problem and goal", "Requirements and rules", "Acceptance scenarios"},
    "CHG": {"Reason and scope", "Before and after"},
    "ADR": {"Context", "Options and decision", "Consequences and revisit conditions"},
    "KNW": {"Overview", "How it works", "Verification and limitations"},
    "LOG": {"Summary", "Previous behavior", "New behavior", "Tests and verification", "Documentation updated"},
}
LEGACY_SECTIONS = {
    "REQ": {"Overview", "Functional requirements", "Acceptance criteria"},
    "CHG": {"Summary", "Current behavior", "Proposed behavior", "Acceptance criteria"},
    "ADR": {"Context", "Decision", "Consequences"},
    "KNW": {"Overview", "Current implementation", "Known limitations"},
}
CHANGE_TYPES = {"feature", "fix", "migration", "refactor", "chore", "docs"}


def required_sections(kind, status, body, legacy_change=False):
    present = set(headings(body))
    legacy = LEGACY_SECTIONS.get(kind)
    use_legacy = legacy is not None and legacy <= present and (kind != "CHG" or legacy_change)
    required = set(legacy if use_legacy else SECTIONS[kind])
    if kind == "CHG":
        if status in ("proposed", "approved", "implementing") and not use_legacy:
            required.add("Acceptance and verification plan")
        if status == "implemented" and not use_legacy:
            required.update({"Implementation result", "Verification", "References"})
    return required


LIST_FIELDS = {
    "REQ": {"dependencies", "related_changes"},
    "CHG": {"related_requirements"},
    "ADR": {"supersedes", "superseded_by"},
    "KNW": {"requirements", "decisions", "components"},
    "LOG": {"requirements", "changes", "decisions", "github_issues", "github_prs", "components"},
}
REFERENCES = {
    "dependencies": "REQ", "related_changes": "CHG", "related_requirements": "REQ",
    "requirements": "REQ", "changes": "CHG", "decisions": "ADR",
    "supersedes": "ADR", "superseded_by": "ADR",
}


def scalar(raw):
    """Parse our deliberately small, documented YAML scalar profile."""
    raw = raw.strip()
    if not raw or raw.startswith(("{", "&", "*", "!", "|", ">")):
        raise ValueError("expected a scalar; nested YAML, aliases, tags and block strings are unsupported")
    if raw.startswith('"'):
        value = json.loads(raw)
        if not isinstance(value, str):
            raise ValueError("quoted value must be a string")
        return value
    if raw.startswith("'"):
        if not raw.endswith("'") or re.search(r"(?<!')'(?!')", raw[1:-1]):
            raise ValueError("invalid single-quoted string")
        return raw[1:-1].replace("''", "'")
    raw = re.split(r"\s+#", raw, maxsplit=1)[0].rstrip()
    if raw in {"null", "~"}:
        return None
    if raw in {"true", "false"}:
        raise ValueError("booleans are unsupported; quote textual values")
    if re.search(r":\s", raw) or any(char in raw for char in "[]{}"):
        raise ValueError("quote scalar values containing YAML punctuation")
    return raw


def inline_list(raw):
    if raw == "[]":
        return []
    # JSON-style arrays avoid ambiguous YAML commas and quoting rules.
    try:
        values = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError('use a JSON-style string array or an indented YAML list') from exc
    if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
        raise ValueError("lists must contain strings only")
    return values


def metadata(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter (start file with ---)")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    result = {}
    current = None
    for line_number, line in enumerate(lines[1:end], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.fullmatch(r"  - (.+)", line)
        if item:
            if current is None or not isinstance(result[current], list):
                raise ValueError(f"line {line_number}: list item without a list field")
            value = scalar(item[1])
            if not isinstance(value, str):
                raise ValueError(f"line {line_number}: lists must contain strings")
            result[current].append(value)
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_]*):(?:\s+(.*))?", line)
        if not match:
            raise ValueError(f"line {line_number}: use flat key: value metadata and two-space list indentation")
        key, raw = match.groups()
        if key in result:
            raise ValueError(f"line {line_number}: duplicate metadata key {key}")
        raw = (raw or "").strip()
        result[key] = [] if not raw else inline_list(raw) if raw.startswith("[") else scalar(raw)
        current = key if not raw else None
    return result, "\n".join(lines[end + 1:])


def without_fenced_code(text):
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def blank_fenced_code(text):
    """Replace fenced examples with spaces while preserving offsets and newlines."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence is None and match:
            fence = match[1]
            lines.append("".join("\n" if char == "\n" else " " for char in line))
        elif fence:
            lines.append("".join("\n" if char == "\n" else " " for char in line))
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
        else:
            lines.append(line)
    return "".join(lines)


def without_html_comments(text):
    """Blank HTML comments outside fenced examples while preserving line positions."""
    lines = []
    in_fence = None
    in_comment = False
    for line in text.splitlines(keepends=True):
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if in_fence:
            lines.append(line)
            if fence and fence[1][0] == in_fence[0] and len(fence[1]) >= len(in_fence):
                in_fence = None
            continue
        if fence and not in_comment:
            in_fence = fence[1]
            lines.append(line)
            continue
        output = []
        index = 0
        while index < len(line):
            if in_comment:
                end = line.find("-->", index)
                if end < 0:
                    output.append("\n" if line.endswith("\n") else "")
                    break
                output.append(" " * (end + 3 - index))
                index = end + 3
                in_comment = False
                continue
            start = line.find("<!--", index)
            if start < 0:
                output.append(line[index:])
                break
            output.append(line[index:start])
            in_comment = True
            index = start
        lines.append("".join(output))
    return "".join(lines)


def without_code(text):
    """Remove fenced blocks and inline code for prose/link scanning."""
    return re.sub(r"(`+).*?\1", "", without_fenced_code(without_html_comments(text)))


def headings(body):
    return re.findall(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", without_fenced_code(without_html_comments(body)), re.M)


def anchors(body):
    seen = {}
    result = set()
    for heading in headings(body):
        heading = re.sub(r"!?\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    visible = without_html_comments(without_fenced_code(body))
    result.update(re.findall(r'\b(?:id|name)=[\"\']([^\"\']+)[\"\']', visible))
    return result


def link_targets(body):
    body = without_code(body)
    definitions = {label.strip().casefold(): target for label, target in re.findall(
        r"^\s{0,3}\[([^]]+)\]:\s*<?([^\s>]+)>?", body, re.M
    )}
    # CommonMark inline links/images, including one level of balanced parentheses.
    for match in re.finditer(r"!?\[[^]\n]*\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)(?:\s+[^\n]*?)?\)", body):
        yield match[1].strip("<>")
    for match in re.finditer(r"!?\[([^]\n]+)\](?:\[([^]\n]*)\])?(?![(:])", body):
        label = (match[2] or match[1]).strip().casefold()
        if label in definitions:
            yield definitions[label]
        elif match[2] is not None:
            yield "!undefined-reference:" + label
    yield from definitions.values()


def classify(relative):
    parts = relative.parts
    if parts[:2] == ("specs", "requirements"):
        if relative.name == "README.md":
            return None
        return "REQ"
    if parts[:2] == ("specs", "changes"):
        if len(parts) == 4 and relative.name == "design.md" and re.fullmatch(rf"{NUMBER}-{SLUG}", parts[2]):
            return None  # Historical split designs are unstructured Markdown.
        return "CHG"
    if parts[0] == "decisions":
        if relative.name == "README.md":
            return None
        return "ADR"
    if parts[0] == "knowledge" and relative.name != "README.md":
        return "KNW"
    if parts[0] == "changelog" and relative.name != "README.md":
        return "LOG"
    return None


def section_contents(body, required):
    body = without_html_comments(body)
    heading_text = blank_fenced_code(body)
    matches = []
    for match in re.finditer(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", heading_text, re.M):
        matches.append((match.start(), match.end(), match[1], match[2]))
    for index, (start, heading_end, depth, title) in enumerate(matches):
        if title not in required:
            continue
        end = len(body)
        for next_start, _, next_depth, _ in matches[index + 1:]:
            if len(next_depth) <= len(depth):
                end = next_start
                break
        yield title, body[heading_end:end]


def empty_sections(body, required):
    return [title for title, content in section_contents(body, required)
            if not has_section_content(content)]


def template_placeholders(text):
    """Recognize instruction placeholders in prose, preserving literal examples."""
    prose = without_code(text)
    # Indented Markdown code is also literal. Fenced and inline code are removed above.
    prose = "\n".join(line for line in prose.splitlines()
                      if not line.startswith(("    ", "\t")))
    for match in re.finditer(r"<([A-Za-z][^<>\n]*)>", prose):
        value = match[1]
        # Avoid HTML attributes and autolinks. Bare HTML tags have no whitespace.
        if "=" in value or "://" in value or "@" in value:
            continue
        if re.match(
            r"(?:describe|enter|insert|replace|fill|provide|record|add|link|links|"
            r"commands?|checks?|tests?|actual|expected|observable|verified|"
            r"established|problem|reason|summary|affected|relative|known|"
            r"implementation|verification|evidence|current|proposed|who|measurable|"
            r"actor|capability|decision|credible|benefits|inspected)(?:,\s*|\s+)",
            value, re.I,
        ) or re.fullmatch(r"condition|action|precondition|test/check|NNNNN|NNNN|YYYY-MM-DD", value):
            yield match[0]
    for match in re.finditer(r"^\s*(?:[-*]\s+)?(?:TODO|TBD|\[TODO\]|\[TBD\])\s*[.!]?\s*$", prose, re.M):
        yield match[0].strip()


def is_legacy_change(relative, identifier):
    if not isinstance(identifier, str) or not re.fullmatch(rf"CHG-{NUMBER}", identifier):
        return False
    number = identifier.split("-", 1)[1]
    return bool(re.fullmatch(
        rf"specs/changes/{number}-{SLUG}(?:\.md|/proposal\.md)", relative.as_posix()
    ))


def has_section_content(text):
    """Require text or code content beyond nested Markdown headings."""
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
            elif line.strip():
                return True
            continue
        if match:
            fence = match[1]
        elif line.strip() and not re.match(r"^\s{0,3}#{1,6}\s+", line):
            return True
    return False


def validate(project_root):
    root = Path(project_root).resolve()
    docs = root / "docs"
    errors = []
    def error(path, message):
        errors.append(f"{path}: {message}")
    for name in ("README.md", "project.md"):
        if not (docs / name).is_file():
            error(docs / name, "required document missing")
    if not docs.is_dir():
        return errors
    texts = {}
    records = {}
    reserved = []
    for path in sorted(docs.rglob("*.md")):
        if not path.resolve().is_relative_to(root):
            error(path, "document symlink escapes project root")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            error(path, f"cannot read UTF-8 document: {exc}")
            continue
        texts[path] = text
        relative = path.relative_to(docs)
        kind = classify(relative)
        for part in relative.parts:
            stem = part[:-3] if part.endswith(".md") else part
            if relative.parts[0] in {"specs", "knowledge", "changelog", "architecture", "decisions", "guides"} and part != "README.md" and not re.fullmatch(SLUG, stem):
                error(path, f"use lowercase kebab-case names: {part}")
        if relative.name == "README.md" and text.startswith("---\n"):
            if relative.parts[:2] == ("specs", "requirements"):
                kind = "REQ"
            elif relative.parts[0] == "decisions":
                kind = "ADR"
            elif relative.parts[0] == "knowledge":
                kind = "KNW"
        if path == docs / "project.md":
            try:
                config, _ = metadata(text)
                reserved = config.get("reserved_ids", [])
                if not isinstance(reserved, list) or any(not isinstance(value, str) or not ID_PATTERN.fullmatch(value) for value in reserved):
                    error(path, "reserved_ids must be a list of valid retired identifiers")
                    reserved = []
                if len(reserved) != len(set(reserved)):
                    error(path, "duplicate reserved_ids")
                owner = config.get("owner")
                if not isinstance(owner, str) or not owner.strip() or re.search(r"<[^>]+>", owner):
                    error(path, "owner must be a nonempty resolved string")
                for policy_key in ("history_policy", "changelog_policy"):
                    if policy_key in config and config[policy_key] not in ("meaningful", "every-issue"):
                        error(path, f"{policy_key} must be meaningful or every-issue")
                if ("history_policy" in config and "changelog_policy" in config
                        and config["history_policy"] != config["changelog_policy"]):
                    error(path, "history_policy and legacy changelog_policy disagree")
            except ValueError as exc:
                error(path, str(exc))
        if kind is None:
            if relative.parts[:2] == ("specs", "changes") and relative.name == "design.md":
                if not (path.parent / "proposal.md").is_file():
                    error(path, "legacy split design requires its existing proposal.md")
            continue
        try:
            fields, body = metadata(text)
        except ValueError as exc:
            error(path, str(exc))
            continue
        required = {"id", "title", "status", "owner"} | LIST_FIELDS[kind]
        required |= {"date", "type", "commit"} if kind == "LOG" else {"created_at", "updated_at"}
        for field in sorted(required - fields.keys()):
            error(path, f"missing required metadata field {field}")
        for field in {"id", "title", "status", "owner"} & fields.keys():
            if not isinstance(fields[field], str) or not fields[field].strip() or re.search(r"<[^>]+>", fields[field]):
                error(path, f"{field} must be a nonempty resolved string")
        identifier = fields.get("id")
        if not isinstance(identifier, str) or not ID_PATTERN.fullmatch(identifier) or not identifier.startswith(kind + "-"):
            error(path, f"invalid {kind} document ID {identifier!r}")
        elif identifier in records:
            error(path, f"duplicate document ID {identifier}; first used in {records[identifier][0]}")
        else:
            records[identifier] = (path, kind, fields)
        if not isinstance(fields.get("status"), str) or fields["status"] not in STATUSES[kind]:
            error(path, f"invalid lifecycle status; expected one of {', '.join(sorted(STATUSES[kind]))}")
        for field in LIST_FIELDS[kind] & fields.keys():
            value = fields[field]
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                error(path, f"{field} must be a list of nonempty strings")
        for field in ("date",) if kind == "LOG" else ("created_at", "updated_at"):
            value = fields.get(field)
            try:
                if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError()
                datetime.date.fromisoformat(value)
            except ValueError:
                error(path, f"{field} must be a valid YYYY-MM-DD date")
        if kind != "LOG" and isinstance(fields.get("created_at"), str) and isinstance(fields.get("updated_at"), str) and fields["updated_at"] < fields["created_at"]:
            error(path, "updated_at precedes created_at")
        if kind == "LOG":
            if not isinstance(fields.get("type"), str) or fields["type"] not in {"feature", "fix", "migration", "refactor", "chore", "docs"}:
                error(path, "invalid changelog type")
            if fields.get("commit") is not None and not isinstance(fields.get("commit"), str):
                error(path, "commit must be a string or null")
        if kind == "CHG" and "type" in fields:
            if not isinstance(fields["type"], str) or fields["type"] not in CHANGE_TYPES:
                error(path, "invalid change type")
        legacy_change = kind == "CHG" and is_legacy_change(relative, identifier)
        sections = required_sections(kind, fields.get("status"), body, legacy_change)
        missing = sections - set(headings(body))
        for section in sorted(missing):
            error(path, f"missing mandatory section: {section}")
        for section in empty_sections(body, sections - missing):
            error(path, f"empty mandatory section: {section}")
        for section, content in section_contents(body, sections - missing):
            for placeholder in template_placeholders(content):
                error(path, f"unfilled template placeholder in {section}: {placeholder}")
        if kind == "REQ" and "priority" in fields and fields["priority"] not in ("low", "medium", "high", "critical"):
            error(path, "priority must be low, medium, high, or critical")
        if kind in {"REQ", "ADR"}:
            prefix = "specs/requirements" if kind == "REQ" else "decisions"
            number = identifier.split("-", 1)[1] if isinstance(identifier, str) else ""
            if relative.name != "README.md" and not re.fullmatch(rf"{prefix}/{re.escape(number)}-{SLUG}\.md", relative.as_posix()):
                error(path, f"filename must match {kind} ID: {prefix}/NNNNN-slug.md")
        if kind == "CHG":
            match = re.fullmatch(
                rf"specs/changes/({NUMBER}-{SLUG}|{DOMAIN})/({SEQUENCE})-{SLUG}\.md",
                relative.as_posix(),
            )
            if match:
                namespace = match[1][:5] if re.match(r"\d{5}-", match[1]) else match[1]
                if identifier != f"CHG-{namespace}-{match[2]}":
                    error(path, "change filename must match CHG ID, group namespace, and record sequence")
                requirements = fields.get("related_requirements", [])
                if namespace.isdigit() and (not isinstance(requirements, list)
                        or f"REQ-{namespace}" not in requirements):
                    error(path, "numbered change group must reference its matching requirement")
            elif not legacy_change:
                error(path, "change filename must match CHG ID: specs/changes/NNNNN-slug/NNNN-slug.md or specs/changes/domain/NNNN-slug.md")
        if kind == "LOG":
            match = re.fullmatch(rf"changelog/({NUMBER}-{SLUG}|{DOMAIN})/({SEQUENCE})-{SLUG}\.md", relative.as_posix())
            if not match:
                error(path, "changelog path must be changelog/NNNNN-slug/NNNN-slug.md or changelog/domain/NNNN-slug.md")
            else:
                namespace = match[1][:5] if re.match(r"\d{5}-", match[1]) else match[1]
                if identifier != f"LOG-{namespace}-{match[2]}":
                    error(path, "changelog ID must match directory namespace and record sequence")
                requirements = fields.get("requirements", [])
                if namespace.isdigit() and (not isinstance(requirements, list) or f"REQ-{namespace}" not in requirements):
                    error(path, "numbered changelog directory must reference its matching requirement")
    for identifier in reserved:
        if identifier in records:
            error(docs / "project.md", f"reserved ID {identifier} is reused by a live document")
    for identifier, (path, kind, fields) in records.items():
        for field, prefix in REFERENCES.items():
            values = fields.get(field, [])
            if not isinstance(values, list):
                continue
            for target in values:
                if not isinstance(target, str) or target not in records or not target.startswith(prefix + "-"):
                    error(path, f"{field}: missing or invalid {prefix} reference {target!r}")
                elif target == identifier:
                    error(path, f"{field}: self-reference {target} is invalid")
        if kind == "ADR":
            successors = fields.get("superseded_by", [])
            if fields.get("status") == "superseded" and not successors:
                error(path, "superseded ADR requires superseded_by")
            if successors and fields.get("status") != "superseded":
                error(path, "ADR with superseded_by must have superseded status")
            for field, reciprocal in (("supersedes", "superseded_by"), ("superseded_by", "supersedes")):
                values = fields.get(field, [])
                for target in values if isinstance(values, list) else []:
                    if target in records and records[target][1] == "ADR":
                        other = records[target][2]
                        reverse = other.get(reciprocal, [])
                        if not isinstance(reverse, list) or identifier not in reverse:
                            error(path, f"{target} must reciprocate via {reciprocal}: {identifier}")
                        if field == "superseded_by" and other.get("status") not in ("accepted", "superseded"):
                            error(path, f"superseding ADR {target} must be accepted or superseded")
    def visit(identifier, active, done):
        if identifier in active:
            error(records[identifier][0], f"supersession cycle involving {identifier}")
            return
        if identifier in done:
            return
        active.add(identifier)
        values = records[identifier][2].get("superseded_by", [])
        for target in values if isinstance(values, list) else []:
            if target in records and records[target][1] == "ADR":
                visit(target, active, done)
        active.remove(identifier)
        done.add(identifier)
    done = set()
    for identifier, (_, kind, _) in records.items():
        if kind == "ADR":
            visit(identifier, set(), done)
    for path, body in texts.items():
        for target in link_targets(body):
            if target.startswith("!undefined-reference:"):
                error(path, target[1:])
                continue
            try:
                parsed = urlsplit(target)
            except ValueError:
                error(path, f"malformed link URL: {target}")
                continue
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not destination.is_relative_to(root):
                error(path, f"local link escapes project root: {target}")
            elif not destination.exists():
                error(path, f"broken local link: {target}")
            elif parsed.fragment and destination.suffix.lower() == ".md":
                try:
                    if unquote(parsed.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                        error(path, f"broken local heading link: {target}")
                except (OSError, UnicodeError) as exc:
                    error(path, f"cannot read link destination {target}: {exc}")
    for directory in (docs / "specs/changes").glob("*"):
        if directory.is_dir() and not re.fullmatch(rf"{NUMBER}-{SLUG}|{DOMAIN}", directory.name):
            error(directory, "change group must be NNNNN-slug or a domain name")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path, help="target repository root containing docs/")
    args = parser.parse_args()
    errors = validate(args.project_root)
    for error in errors:
        print(error)
    print(f"{len(errors)} documentation error(s)")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
