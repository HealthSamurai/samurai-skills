# samurai-skills

Claude Code plugin marketplace by Health Samurai. Contains skills for Aidbox, FHIR, and Health Samurai products.

## Structure

This repo is a **marketplace** (`.claude-plugin/marketplace.json`) containing individual plugins (one per skill) and a bundled plugin (`samurai-skills`) that includes all skills.

```
.claude-plugin/marketplace.json        — marketplace catalog
plugins/
├── samurai-skills/                    — bundled plugin (all skills)
│   ├── .claude-plugin/plugin.json
│   └── skills/
├── aidbox/                            — individual plugin
│   ├── .claude-plugin/plugin.json
│   └── skills/aidbox/SKILL.md
├── aidbox-sql-on-fhir/
│   ├── .claude-plugin/plugin.json
│   └── skills/aidbox-sql-on-fhir/SKILL.md
├── atomic-generate-types/
│   ├── .claude-plugin/plugin.json
│   └── skills/atomic-generate-types/SKILL.md
├── hs-search/
│   ├── .claude-plugin/plugin.json
│   └── skills/hs-search/SKILL.md
└── termbox/
    ├── .claude-plugin/plugin.json
    └── skills/termbox/SKILL.md
```

## Version bumps

After changing any SKILL.md, bump `version` in `plugins/samurai-skills/.claude-plugin/plugin.json`. Claude Code uses the version to detect updates — without a bump, users won't see changes due to caching.

## Adding a new skill

1. Create `plugins/samurai-skills/skills/<skill-name>/SKILL.md` with frontmatter (`name`, `description`) and instructions
2. Use `template/SKILL.md` as a starting point
3. Bump plugin version in `plugins/samurai-skills/.claude-plugin/plugin.json`
4. Skills are auto-discovered from `skills/` — no need to register them anywhere

## Termbox skill

`termbox/references/*.md` are copies of the Termbox agent prompts and MCP page, which are maintained in the `termbox-docs` repo. Don't edit them here. After the docs change, refresh both copies and bump the versions:

```bash
python3 scripts/sync_termbox_skill.py
```

## Testing locally

```bash
claude --plugin-dir ./plugins/samurai-skills
```

Then invoke with `/samurai-skills:<skill-name>`.

## Installation (for users)

```bash
# Add the marketplace
claude plugin marketplace add HealthSamurai/samurai-skills

# Install all skills at once
claude plugin install samurai-skills@samurai-skills

# Or install individual skills
claude plugin install aidbox@samurai-skills
claude plugin install aidbox-sql-on-fhir@samurai-skills
claude plugin install atomic-generate-types@samurai-skills
claude plugin install hs-search@samurai-skills
claude plugin install termbox@samurai-skills
```
