---
name: termbox
description: >
  Termbox, Health Samurai's FHIR terminology server: run it locally with Docker,
  load terminologies (SNOMED CT, LOINC, RxNorm, UCUM, ICD-10, FHIR core, THO, IGs),
  update versions, deploy to Kubernetes, and look up, validate, search or translate
  codes through its FHIR API or MCP server. Use when the user mentions Termbox, wants
  a local FHIR terminology server, needs codes from SNOMED CT, LOINC, RxNorm or other
  code systems, or asks to expand or validate ValueSets.
---

# Termbox

Termbox is Health Samurai's FHIR terminology server. This skill has a step-by-step prompt for each task in `references/`, and the rules that apply to all of them.

## Workflow

1. Pick the prompt for the task from the table below.
2. Read it and follow every step in order. The prompts are self-contained and written for agents, so use them instead of the Termbox documentation pages, `llms.txt` or memory.
3. Finish only when the prompt's verify or wait step passes, then report as the prompt describes.

| Task | Prompt |
| --- | --- |
| Install or run Termbox on this machine, with any set of terminologies | [references/start-local.md](references/start-local.md) |
| List gallery terminologies, editions and versions, or Health Samurai's public resources | [references/gallery.md](references/gallery.md) |
| Find an implementation guide or other FHIR package | [references/packages.md](references/packages.md) |
| Load more content into a running Termbox | [references/add-content.md](references/add-content.md) |
| Move a terminology to another version with no downtime | [references/update-versions.md](references/update-versions.md) |
| Deploy on Kubernetes or roll out a change | [references/kubernetes.md](references/kubernetes.md) |
| Look up, validate, search or translate codes | [references/query.md](references/query.md) |
| Connect an agent to the hosted MCP server | [references/connect-mcp.md](references/connect-mcp.md) |
| Diagnose a problem | [references/troubleshoot.md](references/troubleshoot.md) |
| MCP server reference: tools, examples and limits | [references/mcp.md](references/mcp.md) |

## Rules

- **License:** Start Termbox Locally includes a shared development license in its `docker-compose.yaml`. Use it as given. Never send the user to `/ui/license` and never ask them for a license. Production deployments need a production license from Health Samurai.
- **Loading takes time:** the server answers before content finishes loading, which can take about 20 minutes. Run the prompt's load check. If you stop earlier, tell the user Termbox is still loading and which terminologies are missing.
- **Verify content, not jobs:** a reload job can finish while a source failed, because a missing gallery entry only logs a warning. Check with a code lookup or `CodeSystem?url=...`.
- **`data.yaml` layout:** keep sources in four commented groups, in this order: `# Gallery`, `# Resources`, `# NPM registry` and `# Packages`. Add new sources to the end of their group.
- **Versions:** always give SNOMED CT an edition, such as `http://snomed.info/sct/900000000000207008`. Always pin RxNorm to an exact version, because Termbox can otherwise pick an older release. Quote versions that look like numbers.
- **Endpoint:** use the default FHIR base, `/fhir`.
- **Codes:** never answer with codes from memory. Check them with the API or the MCP tools.

## Querying without running anything

If the Termbox MCP tools are available, such as `find-code`, `lookup-code`, `expand-valueset` and `search-rxnorm`, use them. Otherwise call the hosted FHIR API, which needs no setup:

```bash
BASE=https://tx.health-samurai.io/fhir
curl -s -G "$BASE/CodeSystem/\$lookup" --data-urlencode 'system=http://loinc.org' --data-urlencode 'code=8867-4'
curl -s -G "$BASE/ValueSet/\$expand" --data-urlencode 'url=http://snomed.info/sct?fhir_vs=isa/73211009' --data-urlencode 'filter=type 2' --data-urlencode 'count=10'
```

For a local Termbox, use `BASE=http://localhost:3000/fhir`. More calls are in [references/query.md](references/query.md).

MCP server: `https://tx.health-samurai.io/mcp/sse`, with SSE and Streamable HTTP on the same URL. It serves the hosted content only; the Termbox Docker image has no MCP endpoint. Tools, worked examples and limits are in [references/mcp.md](references/mcp.md).

| System | URL |
| --- | --- |
| SNOMED CT | `http://snomed.info/sct` |
| LOINC | `http://loinc.org` |
| RxNorm | `http://www.nlm.nih.gov/research/umls/rxnorm` |
| UCUM | `http://unitsofmeasure.org` |
| ICD-10 (WHO) | `http://hl7.org/fhir/sid/icd-10` |
| ICD-10-CM | `http://hl7.org/fhir/sid/icd-10-cm` |

Search tips:

- Text search matches words in the display text and doesn't understand synonyms, so try more than one wording.
- Read all the results, because the best match isn't always first.
- Prefer active codes; inactive ones are marked `"inactive": true`.
- In RxNorm relationship filters, write values with the `CUI:` prefix, such as `has_part = CUI:161`.

## Examples

- "Set up a Termbox instance in this folder with LOINC, SNOMED CT International, FHIR core and UCUM" → Start Termbox Locally, keeping only those entries in `data.yaml`.
- "Which SNOMED CT editions can I load?" → Find Terminologies in the Gallery.
- "Add US Core to my Termbox" → Find FHIR Packages, then Add Terminologies and Packages.
- "Move our RxNorm to the latest release" → Update Terminology Versions.
- "Find drugs that have caffeine and acetaminophen as ingredients" → `search-rxnorm`, or the RxNorm example in the Query prompt.
- "Is LOINC 8867-4 valid?" → `lookup-code`, or `CodeSystem/$validate-code` on the hosted API.
