# Ontario Guard Requirements Checker (OBC 9.8.8 / 3.3.1.18)

Determines whether a guard is required and its minimum height, opening limits and climbability rules under the 2024 Ontario Building Code — Part 9 Article 9.8.8 and the Part 3 articles 3.3.1.18 / 3.4.6.5, with the guard load tables.

**Live web tool:** https://dust2engineering.github.io/ontario-guard-requirements-checker/web/

## How it works

- Guard required where the drop exceeds 600 mm (adjacent surface within 1.2 m) — 9.8.8.1.
- Height by location: 900 mm inside a dwelling unit and on low one-unit exterior surfaces; 1,070 mm generally; 920 mm on exit stair flights; 1,500 mm for exterior stairs/landings over 10 m above the adjacent ground.
- Openings block a 100 mm sphere (150 mm triangular at stairs, 200 mm industrial); climbability restricted between 140 and 900 mm (9.8.8.6).

## Data in this repository

- `guard-data.json` — the trigger rule, both height tables with article bases, opening and climbability rules, and the Part 9 / Part 3 guard load tables, from code text and municipal guides quoting it, checked 2026-11-15.
- `guards.py` — command-line checker using the same JSON.

## Command line

```bash
python3 guards.py part9 ext_low 1500
```

## Worked examples

- [backyard-deck-900mm.md](examples/backyard-deck-900mm.md)
- [mezzanine-edge-part3.md](examples/mezzanine-edge-part3.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Structural. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
