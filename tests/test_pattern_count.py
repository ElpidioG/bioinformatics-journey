from ucsd_c1.module1.pattern_count import pattern_count


def test_sample():
    assert pattern_count("GCGCG", "GCG") == 2


def test_multiple_matches():
    assert pattern_count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == 3


def test_overlapping():
    assert pattern_count("AAAA", "AA") == 3


def test_no_match():
    assert pattern_count("ACGT", "TTT") == 0


def test_pattern_longer_than_text():
    assert pattern_count("AC", "ACGT") == 0


def test_match_at_end():
    assert pattern_count("TTTACG", "ACG") == 1
