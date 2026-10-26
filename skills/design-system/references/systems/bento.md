# Bento

Intent: Modular, asymmetric card groups; hierarchy follows content weight.

Semantic starter tokens (adapt to user needs, preserve required project tokens):

```css
:root {
  --bg: #f2f4f7;
  --surface: #ffffff;
  --fg: #111827;
  --muted: #4b5563;
  --border: #d2d9e3;
  --accent: #2259ba;
}
```

Typography: System UI, strong heading/small metadata contrast.
Layout: 12-column grid, 16-24px gutters, intentional card spans.

Components: readable buttons and labels, keyboard-focus styles, explicit loading/empty/error/edge states. Use the brief to choose corner radius and shadows. Verify contrast with an actual checker before claiming WCAG conformance. This is a design direction, not a trademarked brand replica.
