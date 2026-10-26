---
name: design-system
description: "Use when asked to select or create a design system, extract visual style from references, define brand tokens, or generate or revise a DESIGN.md."
---

# Design system

**Goal:** one internally consistent design contract that another workflow can consume, not a new renderer.

1. **Read precedence:** explicit user requirements > existing project `DESIGN.md`, tokens and components (unless user authorizes replacing them) > observed reference evidence > bundled design direction. If existing sources conflict, change only what was authorized and report the conflict.
2. **Choose direction:** consult [the direction index](references/directions.md). Open only the selected direction in `references/systems/`. The six bundled directions are examples, not identity claims about third-party brands.
3. **Handle reference websites:** read only data available through connected host tools. State whether palette/fonts/spacing came from actual DOM/CSS, attached screenshot visual estimates, or user descriptions. Never claim Figma OAuth, browser session inspection, or pixel-perfect measurements without evidence.
4. **Produce:** a `DESIGN.md` with visual principles, semantic colors, typography fallbacks, layout scale, components, states, accessibility and responsive guidance; optionally generate matching `tokens.css`. Existing files are read-only by default; request explicit edit authorization before overwriting.
5. **Validate coherence:** semantic tokens have both light and dark contrast where requested; design token values agree with examples; no bundled external image/font/script dependencies. Use user-owned material with permission.

**Done when:** all emitted tokens are traceable to the specification, `DESIGN.md` and CSS agree where both are provided, and any estimates or accessibility checks not executed are labeled.
