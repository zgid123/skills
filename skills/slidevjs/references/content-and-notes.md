# Content and Presenter Notes

## Purpose

Keep slides focused on the highlights the audience needs to see, and use presenter notes for the detail the speaker needs to explain them. Give each slide a short, concise title that communicates its main idea.

## ✅ Do

- Give each slide one clear communication goal and a short, specific title. Prefer a direct takeaway when it fits the content; use brief topic titles for covers and section dividers.
- Show key takeaways, essential evidence, and useful visuals on the slide. Use concise phrases and emphasize the most important content selectively.
- Put detailed explanations, worked examples, supporting context, and speaking cues in the presenter notes for the relevant slide.
- Keep enough context visible for the audience to understand the message. Leave essential qualifications, units, labels, and evidence needed to interpret a claim on the slide.
- Split content across slides when there are multiple main ideas or the visible content remains crowded.
- Preserve useful existing notes when editing slides, and update them to match changed content. Add notes where supporting detail is needed; simple covers and dividers do not need filler notes.

```md
# Cache repeated reads

- Reuse results for frequent requests
- Set an expiry to limit stale data
- Invalidate cached results after writes

<!--
Explain the cache-aside flow: check the cache, fetch from the source on a miss,
then store the result for later requests.

Example: cache a frequently viewed product description. A price or stock change
requires invalidation so later requests do not keep receiving the previous value.

Ask the audience which data in their application can tolerate a short delay.
-->
```

## ❌ Do not

- Turn a slide into the full speaking script or copy long explanatory paragraphs onto it.
- Use long titles that try to explain every detail, or vague titles that hide the slide's topic.
- Move essential context into notes until the visible slide becomes misleading or incomprehensible.
- Repeat the visible bullets verbatim as the entire note; add the explanation or example the speaker needs.
- Shrink text or choose a decorative component to accommodate too much content.

```md
# A detailed explanation of how caching repeated reads works and all the considerations involved

Caching repeated reads means checking a cache before fetching from the source, fetching on a miss, and storing the result for later requests. Expiry limits stale data, and writes require invalidation. For example, a product description may be cached, but changing its price or stock requires invalidating the previous value.
```

## Presenter note placement

Use an HTML comment block at the end of the relevant slide, after visible content and any slide-local style block, before the next slide separator or the end of the file. Put notes in the numbered article file alongside the slide they explain. A comment earlier in the slide is not treated as its presenter note. See the [Slidev notes syntax](https://sli.dev/guide/syntax#notes).

## Verification

- Check each title is brief, specific, and focused on the slide's main idea, without imposing a fixed word limit.
- Read the visible slide alone: its takeaway and essential context should be understandable.
- Check detailed explanations and examples are in the relevant notes, with no useful source detail silently discarded during condensation.
- Confirm each note comment is at the end of its slide and remains attached to the correct slide when adding separators.
- When preview is available, inspect audience and presenter views to confirm visible content stays concise and notes appear on the intended slide. Report if preview verification is unavailable.
