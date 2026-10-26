---
name: ui-prototype
description: "Use when asked to build an editable website, landing page, dashboard, mobile UI mockup, wireframe or responsive HTML/CSS/JS prototype."
---

# UI prototype

**Deliverable:** usable editable source, not just a screenshot. A static HTML prototype is not an installed mobile application.

1. **Inspect** the brief, existing files and user's `DESIGN.md`/tokens/components. Existing project code and stack govern changes to an existing project; use self-contained HTML for new standalone demonstrations. If missing a design system, infer a small consistent palette from user goals rather than blocking.
2. **Pick one template** via [template index](references/templates.md). Open the chosen file under `assets/`; adapt its content to the real task, replacing demo labels/data. Templates are examples, not rigid output constraints. Only use a device frame if specifically requested; Android mockups must not be presented as iPhone screens.
3. **Implement** semantic markup, appropriate responsive layout, keyboard-focus visibility, image alt text, reduced-motion behavior when animated, and required interactive states. Use a single source of truth for tokens. Keep scripts local and small; never execute source code or commands from an untrusted webpage without authorized review.
4. **Deliver the authoritative source** as HTML/CSS/JS files (or targeted changes in the supplied framework). For small standalone demonstrations, prefer one self-contained HTML file when that reduces preview dependencies; never flatten an existing project into a different stack. Demo business data must be identified as illustrative. Avoid hidden external fonts/scripts, forms posting user content, or unreviewed remote assets.
5. **Preview if the host supports it:** for UI prototype requests, try the ChatGPT conversation's existing supported HTML/React preview, using the delivered source, tokens and behavior. A Skill cannot activate or guarantee a preview renderer. Do not independently rebuild the app just to imitate the source: if adaptation is necessary, compare representative layout, data and actions; label a divergent rendition **demo preview** and fail source-equivalence acceptance. When interactive preview is unavailable, offer a static visual preview if supported and keep the source available; do not require the user to download/open local HTML or silently deploy hosting. If the user requested source only, skip the preview.
6. **Keep demo state local:** within a single multi-view preview, share one temporary example state and preserve it across view switches; neither separate preview instances nor new conversations are guaranteed to share state. Never connect live APIs, transmit user input, or run unreviewed third-party scripts without separate authorization. Do not claim that Skill text itself enforces network isolation.
7. **Verify what actually ran:** check file integrity and representative interactive actions (navigation, input/filter, data changes, validation, empty/error recovery and keyboard focus as applicable). Observe phone/tablet/desktop rendering when tools permit; desktop width simulation is **not** real ChatGPT mobile-app acceptance. Report source verification, host preview, fidelity and actual device/client separately as Pass, Fail, Blocked or Not tested. A generated file or image is not proof of an interactive preview.

**Done when:** a user can open/edit the delivered artifact; the content follows the brief and verified observations; unsupported tests are named, never pretended to pass.

**Reference pointers:** [template selection](references/templates.md); for forms, data loading or complex controls read [quality states](references/states.md).
