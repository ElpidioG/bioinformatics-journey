from ucsd_c1.module1.reverse_complement import reverse_complement


def test_sample():
    assert reverse_complement("AAAACCCGGT") == "ACCGGGTTTT"


def test_reverses_as_well_as_complements():
    # Complement alone would give TTG; reversing it gives GTT.
    assert reverse_complement("AAC") == "GTT"


def test_longer_sequence():
    assert reverse_complement("GATTACA") == "TGTAATC"


def test_own_reverse_complement():
    assert reverse_complement("ACGT") == "ACGT"


def test_single_base():
    assert reverse_complement("A") == "T"


def test_empty():
    assert reverse_complement("") == ""


def test_applying_twice_returns_original():
    pattern = "ATGATCAAGCTT"
    assert reverse_complement(reverse_complement(pattern)) == pattern
