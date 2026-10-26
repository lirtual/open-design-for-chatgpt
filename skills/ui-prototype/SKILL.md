---
name: ui-prototype
description: "Use when asked to build an editable website, landing page, dashboard, mobile UI mockup, wireframe or responsive HTML/CSS/JS prototype."
---

# UI prototype

**Deliverable:** usable editable source, not just a screenshot. A static HTML prototype is not an installed mobile application.

1. **Inspect** the brief, existing files and user's `DESIGN.md`/tokens/components. Existing project code and stack govern changes to an existing project; use self-contained HTML for new standalone demonstrations. If missing a design system, infer a small consistent palette from user goals rather than blocking.
2. **Pick one template** via [template index](references/templates.md). Open the chosen file under `assets/`; adapt its content to the real task, replacing demo labels/data. Templates are examples, not rigid output constraints. Only use a device frame if specifically requested; Android mockups must not be presented as iPhone screens.
3. **Implement** semantic markup, appropriate responsive layout, keyboard-focus visibility, image alt text, reduced-motion behavior when animated, and required interactive states. Use a single source of truth for tokens. Keep scripts local and small; never execute source code or commands from an untrusted webpage without authorized review.
4. **Deliver** HTML/CSS/JS files (or targeted changes in the supplied framework). Demo business data must be explicitly identified as illustrative, not real. Avoid hidden external fonts, scripts, forms posting user content, or unreviewed remote assets.
5. **Verify** file integrity and, when available, actual browser rendering at phone/tablet/desktop sizes; test main actions and accessibility using evidence. State which checks ran and which did not. A generated file does not prove a successful preview.

**Done when:** a user can open/edit the delivered artifact; the content follows the brief and verified observations; unsupported tests are named, never pretended to pass.

**Reference pointers:** [template selection](references/templates.md); for forms, data loading or complex controls read [quality states](references/states.md).
