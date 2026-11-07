"""Module 1 challenge: PatternCount.

Count how many times Pattern appears in Text, including overlapping matches.

Example:
    pattern_count("GCGCG", "GCG") -> 2   (GCG at position 0 and position 2)

Usage:
    py ucsd-c1/module1/pattern_count.py GCGCG GCG
"""

import sys


def pattern_count(text: str, pattern: str) -> int:
    """Return the number of (possibly overlapping) occurrences of pattern in text."""

    count = 0
    for i in range(len(text) - len(pattern)+1):
        if text[i:len(pattern)+i] == pattern:
            count += 1
    return count



if __name__ == "__main__":
    text, pattern = sys.argv[1], sys.argv[2]
    print(pattern_count(text, pattern))
