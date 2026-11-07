import pytest

from gc_content import gc_content, parse_fasta


def test_all_gc():
    assert gc_content("GGCC") == 1.0


def test_no_gc():
    assert gc_content("ATAT") == 0.0


def test_half_gc():
    assert gc_content("ACGT") == 0.5


def test_lowercase():
    assert gc_content("acgt") == 0.5


def test_ignores_n():
    assert gc_content("GCNN") == 1.0


def test_empty():
    assert gc_content("") == 0.0


def test_invalid_base():
    with pytest.raises(ValueError):
        gc_content("ACGX")


def test_parse_fasta():
    text = ">seq1 description\nACGT\nGG\n\n>seq2\nTTTT\n"
    assert parse_fasta(text) == {"seq1": "ACGTGG", "seq2": "TTTT"}


def test_parse_fasta_missing_header():
    with pytest.raises(ValueError):
        parse_fasta("ACGT\n>seq1\nGG")
