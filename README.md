# Health Samurai Skills

Claude Code skills for Health Samurai products and healthcare development.

## Installation

```bash
# Add as plugin source
claude plugin add /path/to/samurai-skills
```

## Skills

| Skill | Description |
|-------|-------------|
| `aidbox` | Aidbox FHIR platform — API, configuration, access control, terminology |
| `aidbox-sql-on-fhir` | SQL on FHIR with Aidbox — ViewDefinitions, $materialize, sof schema |

## Creating a new skill

Use `template/SKILL.md` as a starting point. Each skill is a folder under `skills/` with at minimum a `SKILL.md` file.

## Structure

```
skills/
├── aidbox/              # Aidbox FHIR platform
│   ├── SKILL.md
│   └── references/      # On-demand reference docs
├── aidbox-sql-on-fhir/  # SQL on FHIR ViewDefinitions & analytics
│   └── SKILL.md
└── ...
```
