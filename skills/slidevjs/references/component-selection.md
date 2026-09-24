# Component Selection

## Purpose

Choose `@alphacifer/slidev-addon-theme` components according to the relationship in the content. The component should make that relationship easier to understand; it should not be decoration added after the slide is written.

Slidev auto-registers addon components, so use the component tags directly in Markdown without importing them.

## Selection workflow

1. State the slide's single communication goal.
2. Identify the relationship among its ideas: sequence, cycle, equal facets, hub-and-spoke, comparison, attribution, quotation, or transition.
3. Choose the component whose visual grammar matches that relationship and supported item count.
4. Reshape the copy to fit the component: use short headings and one concise supporting statement per item.
5. Use ordinary Markdown, code blocks, diagrams, charts, or images when no addon component improves comprehension.

Do not force every slide into a custom component. Avoid placing multiple primary diagrams on one slide, using a fixed-count component with the wrong number of ideas, or shrinking dense paragraphs until they become unreadable. Split overloaded material across slides.

## Quick decision table

| Content relationship | Use | Best fit |
|---|---|---|
| Linear workflow with 2-4 stages | `ArcArrowProcess` | A clearly ordered procedure or pipeline where arrows should carry the narrative |
| Sequential step cards | `ChevronCard` | 2-4 compact stages in a grid where directional chevrons reinforce progression |
| Numbered steps or feature highlights | `HorizCard` | 2-4 compact cards with optional icons and flexible grid placement |
| Parallel items in a horizontal row | `VertCard` | 3-4 independent categories, features, or principles with similar visual weight |
| Three ideas in a repeating cycle | `ArrowTriad` | Feedback loops and mutually reinforcing stages |
| Exactly three equal, interconnected concepts | `HexTriad` | Pillars, principles, or dimensions that form one cohesive whole |
| Three rich options with optional drill-down | `GearTriad` | A high-impact overview followed by click-driven details for each option |
| Exactly four equal concepts around one theme | `RectOrbitTetrad` | Four pillars, quadrants, or balanced strategic dimensions |
| One topic with 3-4 related callouts | `ArcOrbit` | Capabilities, architecture pillars, or features radiating from one hub |
| Two alternatives with 3-4 matched points each | `ArcComparison` | Narrative head-to-head trade-offs such as current vs. proposed |
| Two to four alternatives across many criteria | `TableComparison` | Data-dense feature matrices, stack evaluations, or studies with more than four criteria |
| One memorable statement | `Quote` | A quotation or principle that deserves a dedicated slide |
| Dramatic hero or divider title | `ReflectedTitle` | A short title on a hero slide or dark banner |
| Title that moves before content appears | `TransitionHeading` | Click-driven intro slides, especially with `shifting-intro` |
| Presenter and date attribution | `Speaker` | Cover, introduction, or closing attribution |
| Standalone formatted date | `Date` | Custom covers or footers that do not need speaker attribution |
| Audience questions | `QnA` | Final or penultimate Q&A transition |
| Closing thank-you artwork | `ThanksContent` or `thanks` layout | The final slide |

## Cards

### `ChevronCard`

**Purpose:** Show compact sequential steps as horizontal cards with directional chevron badges.

**When to use:** Use for onboarding stages, delivery pipelines, sprint phases, or another sequence that benefits from visible direction. A 2x2 grid works especially well for four steps.

**Avoid when:** The items are unordered categories or need long explanations. Prefer `VertCard` for equal independent categories and `ArcArrowProcess` when the arrows themselves should form the main process diagram.

**Composition:** `ChevronCard` with `ChevronCardHeading` and `ChevronCardContent`; use `step` and `color` on the root.

### `HorizCard`

**Purpose:** Present numbered steps or feature highlights in flexible horizontal cards with optional icons.

**When to use:** Use for 2-4 concise steps, capabilities, benefits, or feature highlights arranged in a grid. Choose this over `ChevronCard` when the items need icons or when strict directional flow is secondary.

**Avoid when:** The content needs a tall side-by-side comparison or a connected process path.

**Composition:** Use `title` and `description` props for simple cards, or compose `HorizCardHeading`, `HorizCardContent`, and the `icon` slot.

### `VertCard`

**Purpose:** Present parallel items in tall cards with optional step badges, icons, and dividers.

**When to use:** Use for 3-4 equal-weight concepts displayed across a row, such as capabilities, principles, audience groups, or independent phases.

**Avoid when:** The items form a cycle, explicit arrow sequence, or central relationship. Use `variant="none"` for categories that should not look sequential.

**Composition:** `VertCard` with `VertCardTitle` and `VertCardContent`; use `variant="outside"` for numbered steps and `variant="none"` for unordered categories.

## Processes and conceptual relationships

### `ArcArrowProcess`

**Purpose:** Make a 2-4 stage linear workflow the main visual narrative through interlocking curved arrows.

**When to use:** Use for procedures, development lifecycles, data pipelines, request flows, or chronological stages with a definite start and end.

**Avoid when:** The process repeats indefinitely; use `ArrowTriad` for a three-stage cycle. Do not use it for unordered pillars.

**Composition:** `ArcArrowProcess` contains one `ArcArrowProcessCallout` per stage, each with `ArcArrowProcessHeading` and `ArcArrowProcessContent`. Set `count` to `2`, `3`, or `4`, or let it infer the count from callouts.

### `ArrowTriad`

**Purpose:** Visualize exactly three concepts that flow into one another as a cycle or interdependent system.

**When to use:** Use for feedback loops, recurring development cycles, continuous improvement, or three stages whose outputs feed the next stage.

**Avoid when:** The three ideas are equal pillars without directional movement; use `HexTriad`. Do not invent a cycle merely because there are three bullets.

**Composition:** `ArrowTriad` contains three `ArrowTriadCallout` elements with `ArrowTriadHeading`, `ArrowTriadContent`, and optional `ArrowTriadIcon`.

### `HexTriad`

**Purpose:** Present exactly three equal-weight, interconnected concepts as one cohesive model.

**When to use:** Use for three principles, architectural pillars, research dimensions, or values that jointly define the central idea.

**Avoid when:** The concepts are sequential or one is more important than the others. Use `ArrowTriad` for cyclical movement and cards for independent unequal content.

**Composition:** `HexTriad` contains three `HexTriadCallout` elements, each using `HexTriadBadge`, `HexTriadHeading`, and `HexTriadContent`.

### `GearTriad`

**Purpose:** Provide a visually rich three-option overview that can expand into click-driven detail panels.

**When to use:** Use when exactly three methodologies, solutions, workstreams, or research approaches each have 3-4 supporting details. It is strongest when the talk first shows the overview, then explores each option.

**Avoid when:** A static three-item overview is sufficient; prefer `HexTriad` or `ArrowTriad` for a lighter slide. Avoid it when the audience needs to compare the options across common criteria; use a comparison component.

**Composition:** Use three `GearTriadCallout` elements with `GearTriadHeading` and `GearTriadDescription`. Add one `GearTriadContents` group per option, containing `GearTriadContent` items, only when drill-down is useful.

### `RectOrbitTetrad`

**Purpose:** Present exactly four equally weighted concepts around a central theme.

**When to use:** Use for four pillars, four quadrants, balanced strategy frameworks, or four system qualities where symmetry communicates equal importance.

**Avoid when:** The items are sequential, unequal, or do not share one center. Use cards for looser groups and `ArcOrbit` for three or four supporting callouts on one side.

**Composition:** `RectOrbitTetrad` contains four `RectOrbitTetradCallout` elements with `RectOrbitTetradHeading`, `RectOrbitTetradContent`, and optional icons.

### `ArcOrbit`

**Purpose:** Break one central topic into three or four related callouts arranged along a single edge-anchored arc.

**When to use:** Use for capabilities, benefits, architectural qualities, or feature breakdowns that belong to one hub. Choose `position="left"` or `position="right"` to leave space for the surrounding composition.

**Avoid when:** Two opposing alternatives must be compared; use `ArcComparison`. Avoid it for a chronological process because the orbit does not imply a clear start-to-finish path.

**Composition:** `ArcOrbit` contains `ArcOrbitTitle` and `ArcOrbitContents`; each `ArcOrbitCallout` uses `ArcOrbitBadge`, `ArcOrbitHeading`, and `ArcOrbitContent`. Set `count` to `3` or `4`.

## Comparisons

### `ArcComparison`

**Purpose:** Compare two alternatives through opposing hubs and three or four matched narrative points per side.

**When to use:** Use for current vs. proposed, monolith vs. microservices, manual vs. automated, or another head-to-head story where each side has corresponding qualitative points.

**Avoid when:** There are more than two alternatives, more than four criteria, or precise cell-by-cell evaluation matters. Use `TableComparison` for those cases.

**Composition:** `ArcComparison` contains `ArcComparisonLeft` and `ArcComparisonRight`. Each side uses `ArcComparisonTitle`, `ArcComparisonContents`, and matched `ArcComparisonOrbit` items with badge, heading, and content children. Keep the same `count` and criterion order on both sides.

### `TableComparison`

**Purpose:** Compare two to four alternatives across a shared set of explicit criteria in a compact matrix.

**When to use:** Use for technology selection, feature matrices, experiment variants, architecture evaluations, or any comparison with more than four criteria.

**Avoid when:** The slide needs a persuasive two-sided narrative rather than dense scanning; use `ArcComparison`. Split the table when cells require paragraph-length prose.

**Composition:** `TableComparison` contains `TableComparisonCols` with one `TableComparisonCol` per alternative, then `TableComparisonRows` with one `TableComparisonRow` per criterion and one `TableComparisonCell` per column.

## Core presentation components

### `Quote`

**Purpose:** Give one memorable statement or principle strong visual emphasis.

**When to use:** Use on a dedicated insight slide with short quote text and optional author attribution. Do not use it as a decorative wrapper for ordinary prose or several quotations.

### `ReflectedTitle`

**Purpose:** Render a short hero heading with a mirrored reflection.

**When to use:** Use sparingly for a dramatic hero slide or major divider, preferably over a dark or high-contrast background. Do not use it for normal slide titles or long headings.

### `TransitionHeading`

**Purpose:** Move a title from a centered intro state to the normal title position as body content is revealed.

**When to use:** Use with click-driven article introductions and the `shifting-intro` layout. Do not add it when the layout already provides the intended title behavior without custom click logic.

### `Speaker`

**Purpose:** Show presenter or team attribution with a consistently formatted date.

**When to use:** Use on the cover and optionally on introduction or closing slides. Prefer the `team` prop for multiple presenters. Follow the Slidev skill's scaffold-default and author-edit preservation rule for `date`.

### `Date`

**Purpose:** Render a standalone date in `dd/MM/yyyy` format.

**When to use:** Use inside a custom cover, footer, or metadata block that does not need speaker attribution. Use `Speaker` when presenter names and date belong together.

### `QnA`

**Purpose:** Signal the audience question period with an animated Q&A title.

**When to use:** Use on the final or penultimate slide when the presentation explicitly includes a question period. Do not add it automatically when the requested ending is only a thank-you slide.

### `ThanksContent`

**Purpose:** Render the closing thank-you composition and its geometric accents.

**When to use:** Prefer the zero-configuration `thanks` layout for the final slide. Use `ThanksContent` directly only when a custom closing layout or placement is required.
