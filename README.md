# OpenDesign for ChatGPT

Independent, unofficial Skills-only adaptation of [nexu-io/open-design](https://github.com/nexu-io/open-design) for ChatGPT. No MCP server, daemon, database, or external runtime.

Five explicit workflows: `design-brief`, `design-system`, `ui-prototype`, `design-refine`, `design-review`. Includes five static HTML prototype seeds and six design-direction references.

For provenance see `ATTRIBUTION.md`; for implementation requirements see [Spec #1](https://github.com/lirtual/open-design-for-chatgpt/issues/1).

## Validation

```sh
python3 -m pip install PyYAML==6.0.2
python3 scripts/check.py
```

Private installation and real agent behavior are a separate verification gate. This plugin does not claim to provide OpenDesign Studio or a native mobile application.
