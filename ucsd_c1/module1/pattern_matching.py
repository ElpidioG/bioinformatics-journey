"""Module 1 challenge: PatternMatching.

Find all starting positions (0-based) where Pattern appears in Genome, in
increasing order. Occurrences may overlap.

Example:
    pattern_matching("ATAT", "GATATATGCATATACTT") -> [1, 3, 9]   (matches at 1 and 3 overlap)

Usage:
    py ucsd_c1/module1/pattern_matching.py ATAT GATATATGCATATACTT
"""

import sys


def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Return the 0-based starting positions of pattern in genome, in increasing order."""
    size = len(pattern)
    matching = []
    for c in range(len(genome)):
         if genome[c:size+c] == pattern:
            matching.append(c)
    return matching
           
           






if __name__ == "__main__":
    pattern, genome = sys.argv[1], sys.argv[2]
    print(" ".join(str(position) for position in pattern_matching(pattern, genome)))
