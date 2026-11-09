from ucsd_c1.module1.pattern_matching import pattern_matching


def test_sample():
    assert pattern_matching("ATAT", "GATATATGCATATACTT") == [1, 3, 9]


def test_overlapping():
    assert pattern_matching("AA", "AAAA") == [0, 1, 2]


def test_matches_at_start_and_end():
    assert pattern_matching("ACG", "ACGTTACG") == [0, 5]


def test_single_base():
    assert pattern_matching("A", "CACA") == [1, 3]


def test_pattern_equals_genome():
    assert pattern_matching("ACGT", "ACGT") == [0]


def test_no_match():
    assert pattern_matching("TTT", "ACGT") == []


def test_pattern_longer_than_genome():
    assert pattern_matching("ACGT", "AC") == []
