"""Module 1 challenge: ReverseComplement.

Return the reverse complement of a DNA string: reverse Pattern, then replace
each base with its complement (A <-> T, C <-> G).

Example:
    reverse_complement("AAAACCCGGT") -> "ACCGGGTTTT"   (reversed: TGGCCCAAAA, then complemented)

Usage:
    py ucsd_c1/module1/reverse_complement.py AAAACCCGGT
"""

import sys


def reverse_complement(pattern: str) -> str:
    """Return the reverse complement of the DNA string pattern."""

    reversed= ""
    for c in pattern:
        reversed = c+reversed

    reverse_complement =""

    for c in reversed:
        if c == "A":
            reverse_complement = reverse_complement + "T"
        elif c == "T":
                reverse_complement = reverse_complement + "A"
        elif c == "C":
            reverse_complement = reverse_complement + "G"
        elif c == "G":
            reverse_complement = reverse_complement + "C"

    return reverse_complement


if __name__ == "__main__":
    print(reverse_complement(sys.argv[1]))
