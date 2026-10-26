# Minimal

Intent: Quiet structure with careful typography and generous whitespace.

Semantic starter tokens (adapt to user needs, preserve required project tokens):

```css
:root {
  --bg: #fafaf9;
  --surface: #ffffff;
  --fg: #202020;
  --muted: #606060;
  --border: #dfdfdd;
  --accent: #375b4b;
}
```

Typography: System UI, 15-16px body, fewer heading sizes.
Layout: 960px content, single column, 8px spacing rhythm.

Components: readable buttons and labels, keyboard-focus styles, explicit loading/empty/error/edge states. Use the brief to choose corner radius and shadows. Verify contrast with an actual checker before claiming WCAG conformance. This is a design direction, not a trademarked brand replica.
