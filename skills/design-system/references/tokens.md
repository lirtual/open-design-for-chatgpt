# Token contract

Preserve existing token names and CSS-variable conventions in an existing project. For a new standalone prototype, these six roles are enough:

```css
:root {
  --bg: #f8f9fa;
  --surface: #ffffff;
  --fg: #17191c;
  --muted: #575f6a;
  --border: #d5d9df;
  --accent: #1f56b5;
}
```

Ensure contrast for body text, interactive elements and visible focus. Tokens are examples, not claims of compliance. For optional dark theme, define a separate color-mode contract. Fonts should always provide local/system fallbacks. When generating `DESIGN.md`, include color roles, typography hierarchy, spacing/grid, surfaces, components, responsive rules, state coverage and intentional exclusions. If user's brief demands palette variation, adjust tokens; do not claim fixed token values suit every brand.
