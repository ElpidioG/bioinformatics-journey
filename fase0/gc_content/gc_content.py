"""Fase 0 readiness test: compute the GC content of DNA sequences.

Usage:
    python gc_content.py ACGTGGCC
    python gc_content.py --fasta sequences.fasta
"""

import argparse

VALID_BASES = set("ACGTN")


def gc_content(seq: str) -> float:
    """Return the GC fraction (0.0-1.0) of a DNA sequence, ignoring N."""
    seq = seq.upper()
    invalid = set(seq) - VALID_BASES
    if invalid:
        raise ValueError(f"Invalid bases in sequence: {sorted(invalid)}")
    counted = len(seq) - seq.count("N")
    if counted == 0:
        return 0.0
    return (seq.count("G") + seq.count("C")) / counted


def parse_fasta(text: str) -> dict[str, str]:
    """Parse FASTA text into {record_id: sequence}."""
    records: dict[str, str] = {}
    current = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            current = line[1:].split()[0]
            records[current] = ""
        elif current is None:
            raise ValueError("Sequence data found before a FASTA header")
        else:
            records[current] += line
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("sequence", nargs="?", help="DNA sequence")
    group.add_argument("--fasta", help="path to a FASTA file")
    args = parser.parse_args()

    if args.fasta:
        with open(args.fasta) as f:
            records = parse_fasta(f.read())
        for record_id, seq in records.items():
            print(f"{record_id}\t{gc_content(seq) * 100:.2f}%")
    else:
        print(f"{gc_content(args.sequence) * 100:.2f}%")


if __name__ == "__main__":
    main()
