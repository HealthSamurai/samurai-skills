# Health Samurai Skills

Health Samurai skills for Aidbox, FHIR, and healthcare development.

## Installation

Install all skills:

```bash
npx skills add HealthSamurai/samurai-skills
```

Install a specific skill by name:

```bash
npx skills add HealthSamurai/samurai-skills --skill aidbox
npx skills add HealthSamurai/samurai-skills --skill aidbox-sql-on-fhir
npx skills add HealthSamurai/samurai-skills --skill atomic-generate-types
npx skills add HealthSamurai/samurai-skills --skill hs-search
npx skills add HealthSamurai/samurai-skills --skill termbox
```

Install globally instead of per-project:

```bash
npx skills add HealthSamurai/samurai-skills -g
```

From the Claude Code marketplace:

```bash
claude plugin install aidbox@samurai-skills
claude plugin install aidbox-sql-on-fhir@samurai-skills
claude plugin install atomic-generate-types@samurai-skills
claude plugin install hs-search@samurai-skills
claude plugin install termbox@samurai-skills
```

## Skills

| Skill | Description |
|-------|-------------|
| `aidbox` | Aidbox FHIR platform — API, configuration, access control, terminology |
| `aidbox-sql-on-fhir` | SQL on FHIR with Aidbox — ViewDefinitions, $materialize, sof schema |
| `atomic-generate-types` | Generate FHIR types using @atomic-ehr/codegen — TypeScript, Python, C# |
| `hs-search` | Search health-samurai.io — docs, blog, case studies, examples |
| `termbox` | Termbox FHIR terminology server — run locally, load and update terminologies, query codes via FHIR API or MCP |

### `aidbox`

Aidbox guidance for FHIR REST API work, Docker setup, init bundles, access policies, subscriptions, terminology, custom resources, and other Aidbox-specific features.

Examples:
- "Set up a new Aidbox instance with Docker Compose"
- "Create an AccessPolicy that allows my app to read and update Patient resources"
- "Show me how to POST a transaction Bundle to `/fhir` in Aidbox"

### `aidbox-sql-on-fhir`

SQL on FHIR guidance for Aidbox analytics workflows with `ViewDefinition`, `$materialize`, `$run`, and queries against the `sof` schema.

Examples:
- "Create a ViewDefinition for patient demographics"
- "Materialize this ViewDefinition into the `sof` schema"
- "Write a SQL query for a body-weight dashboard from `sof.body_weight`"

### `atomic-generate-types`

FHIR type generation with `@atomic-ehr/codegen` for TypeScript, Python, and C#. Covers setup, generation scripts, tree-shaking, and package selection.

Examples:
- "Generate R4 Patient and Bundle types for a TypeScript project"
- "Set up `scripts/generate-types.ts` for a Python project"
- "Update the tree-shake config to include Observation and Encounter"

### `hs-search`

Search Health Samurai docs, articles, landing pages, and examples when you need current product details or the exact documentation page.

Examples:
- "Find the Aidbox docs for access policies"
- "Search Health Samurai pricing pages"
- "Find examples for loading FHIR implementation guides in Aidbox"

### `termbox`

Termbox FHIR terminology server: start it locally with chosen terminologies, find gallery content and FHIR packages, add or update terminologies, deploy to Kubernetes, and look up, validate or search codes through the FHIR API or the hosted MCP server. Each task follows a prompt from the [Termbox docs](https://www.health-samurai.io/docs/termbox/agents).

Examples:
- "Set up a Termbox instance in this folder with LOINC, SNOMED CT International, FHIR core and UCUM"
- "Add US Core to my Termbox"
- "Find drugs that have caffeine and acetaminophen as ingredients"

## Creating a new skill

Use `template/SKILL.md` as a starting point. Each skill is a folder under `plugins/samurai-skills/skills/` with a `SKILL.md` file. See [Skills docs](https://code.claude.com/docs/en/skills) for the frontmatter format.

## Structure

```
.claude-plugin/
└── marketplace.json                    # Marketplace catalog
plugins/
└── samurai-skills/                     # Plugin
    ├── .claude-plugin/
    │   └── plugin.json                 # Plugin manifest
    └── skills/
        ├── aidbox/SKILL.md
        ├── aidbox-sql-on-fhir/SKILL.md
        ├── atomic-generate-types/SKILL.md
        ├── hs-search/SKILL.md
        └── termbox/
            ├── SKILL.md
            └── references/         # Step-by-step prompts for each Termbox task
template/
└── SKILL.md                            # Template for new skills
```
