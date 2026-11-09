from pathlib import Path

import pytest

from ucsd_c1.module1.frequent_words import frequent_words

DATA_DIR = Path(__file__).resolve().parent.parent / "ucsd_c1" / "module1" / "FrequentWords"

# What each dataset checks, from FrequentWords.pdf.
CASES = {
    1: "sample dataset",
    2: "counts the last k-mer in Text",
    3: "counts overlapping occurrences",
    4: "reports all tied k-mers",
    5: "counts the k-mer at the very start of Text",
}


def load_case(n):
    text, k = (DATA_DIR / "inputs" / f"input_{n}.txt").read_text().split()
    expected = (DATA_DIR / "outputs" / f"output_{n}.txt").read_text().split()
    return text, int(k), expected


@pytest.mark.parametrize("n", CASES, ids=[f"case{n}: {d}" for n, d in CASES.items()])
def test_dataset(n):
    text, k, expected = load_case(n)
    # Order of tied k-mers doesn't matter, so compare sorted.
    assert sorted(frequent_words(text, k)) == sorted(expected)


def test_no_duplicates_in_result():
    # ACGTTGCATGTCGCATGATGCATGAGAGCT: CATG and GCAT each appear 3 times,
    # but each should be reported once.
    result = frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    assert len(result) == len(set(result))
