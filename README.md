# Bioinformatics Journey

My learning log for bioinformatics: from a Python readiness check (Fase 0)
through the UCSD *Bioinformatics Specialization*, Course 1 (*Finding Hidden
Messages in DNA*). Each challenge gets its own script, and every script has tests.

## Structure

```
bioinformatics-journey/
├── README.md          # what this repo is + progress table
├── fase0/
│   └── gc_content/    # readiness test script + tests
├── ucsd-c1/
│   ├── module1/       # one .py per challenge + notes.md
│   ├── module2/
│   ├── module3/
│   └── module4/
└── tests/             # shared tests for the course challenges
```

## Running the tests

```bash
pip install pytest
pytest
```

## Progress

| Phase   | Module / Topic                          | Status         | Notes |
|---------|-----------------------------------------|----------------|-------|
| Fase 0  | GC content (readiness test)             | 🟡 In progress | [fase0/gc_content](fase0/gc_content/) |
| UCSD C1 | Module 1: Where in the genome does replication begin? | ⬜ Not started | [notes](ucsd-c1/module1/notes.md) |
| UCSD C1 | Module 2: Skew, mismatches, DnaA boxes  | ⬜ Not started | [notes](ucsd-c1/module2/notes.md) |
| UCSD C1 | Module 3: Motif finding                 | ⬜ Not started | [notes](ucsd-c1/module3/notes.md) |
| UCSD C1 | Module 4: Randomized motif search       | ⬜ Not started | [notes](ucsd-c1/module4/notes.md) |

Legend: ⬜ Not started · 🟡 In progress · ✅ Done
