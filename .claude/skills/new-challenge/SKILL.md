---
name: new-challenge
description: Scaffold a new UCSD bioinformatics course challenge - a script template with a stub function, pytest tests built from the challenge's sample datasets (usually a PDF), and a row in the module's notes.md. Use when the user shares a challenge PDF/problem statement or says they're starting a new challenge.
---

# New challenge scaffold

The user is learning by solving these challenges themselves. **Never implement the
solution** — the function body is always a stub. Your job is the scaffolding around it.

## 1. Gather the facts

- **Challenge name** (e.g. `FrequentWords`) and **module** (e.g. `ucsd_c1/module1`).
  Infer from the PDF title, the file the user has open, or ask.
- **Problem statement**: input, output, and every test case (input, expected output,
  and the description of what each case checks). Usually from an attached PDF.
- Look in `<module>/<ChallengeName>/` for existing `inputs/input_N.txt` and
  `outputs/output_N.txt`. If they're missing, create them from the PDF: one input
  value per line, output exactly as the PDF shows it. Skip cases with no data in
  the PDF (e.g. a "full-size graded dataset") and tell the user.

## 2. Script template: `<module>/<snake_name>.py`

If the file exists and has content, show the user and ask before overwriting.
Follow this shape (from `ucsd_c1/module1/pattern_count.py`):

```python
"""Module N challenge: ChallengeName.

One or two sentences restating the problem, including gotchas the test cases
call out (overlaps, ties, ...).

Example:
    func_name(<sample input>) -> <sample output>   (short why)

Usage:
    py <module>/<snake_name>.py <sample args>
"""

import sys


def func_name(arg: type, ...) -> return_type:
    """One-line description of the return value."""

    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    # parse sys.argv into the right types, call the function,
    # print the result in the PDF's output format (lists -> " ".join)
```

- Use the PDF's parameter order and snake_case names (Text -> `text`, k -> `k`).
- Use the sample dataset (case 1) for the Example and Usage lines.

## 3. Tests: `tests/test_<snake_name>.py`

Import as `from <module.dotted.path>.<snake_name> import func_name` (pyproject sets
`pythonpath = ["."]`). Load cases from the data files rather than inlining them:

```python
DATA_DIR = Path(__file__).resolve().parent.parent / "<module>" / "<ChallengeName>"

# What each dataset checks, from <ChallengeName>.pdf.
CASES = {1: "sample dataset", 2: "...", ...}

def load_case(n): ...  # read input_n.txt / output_n.txt, convert types

@pytest.mark.parametrize("n", CASES, ids=[f"case{n}: {d}" for n, d in CASES.items()])
def test_dataset(n): ...
```

- If the output is an unordered collection, compare `sorted(...)`.
- Add a few small hand-written tests for edge cases the datasets don't cover
  (duplicates in results, empty/no-match, pattern longer than text, ...).
  Keep them correct — derive expected values by hand and double-check.

## 4. Verify the tests without touching the stub

Run pytest with a throwaway reference implementation injected into `sys.modules`,
so the user's file stays untouched:

```bash
py -c "
import sys, types, pytest
m = types.ModuleType('<dotted.module.path>')
def f(...): ...  # quick reference solution
m.func_name = f
sys.modules[m.__name__] = m
sys.exit(pytest.main(['-q', 'tests/test_<snake_name>.py']))
"
```

All tests must pass. Do not write the reference solution anywhere on disk or show it
to the user unless they ask.

## 5. notes.md

Add a row to the Challenges table in `<module>/notes.md`:
`| ChallengeName | [snake_name.py](snake_name.py) | ⬜ |`

## 6. Report

Briefly tell the user: files created, the function signature the tests expect,
which cases were skipped, and `pytest tests/test_<snake_name>.py` to run them.

## 7. Before uploading to the repo

Once the challenge is solved, and before any commit or push, run the full suite from
the repo root:

```bash
py -m pytest -v
```

Every test must pass. If any fail, show the user the output and do not commit or push.
