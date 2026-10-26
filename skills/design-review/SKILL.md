---
name: design-review
description: "Use when asked for a read-only design, UX, responsive, accessibility or visual-quality audit of a screenshot, design file, webpage or existing UI."
---

# Design review

**Read-only by default.** Review never silently modifies files, branches or deployments. Any subsequent fix is a separately authorized `design-refine` task.

1. **Evidence gate:** inspect real user-provided screens or authoritative source, plus available browser/DOM or ChatGPT preview when actually accessible. Distinguish a source-backed interactive preview from an explicitly labeled demo rendition; compare meaningful view, data and interaction behavior before claiming equivalence. For each claim mark evidence as screenshot observation, source observation, measured check, or inference. Never infer mobile ChatGPT compatibility, keyboard behavior or real browser navigation from a desktop-only or static screenshot.
2. **Evaluate critical paths:** content hierarchy, typography, contrast, touch target/focus, interaction feedback, loading/empty/error/edge states, responsive behavior, and consistency with existing tokens. Open [review rubric](references/rubric.md) only for applicable branches.
3. **Report** issues by impact (blocking, important, polish) with concrete location, observable issue, evidence, small suggested fix and how to verify. Call out unknowns instead of guessing.
4. **Completion:** concise ordered findings plus passed observations and remaining untested checks. Report the actual host/device separately: preview shown, key interactions, source fidelity and real mobile-client checks can each be Pass, Fail, Blocked or Not tested. A recommendation is not proof of an issue fixed.

Avoid invented statistics, falsely precise ratings, reading passwords/cookies, and unsupported certification or compliance claims.
