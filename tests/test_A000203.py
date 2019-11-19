from oeis import A000203
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000203() == [
        1,
        3,
        4,
        7,
        6,
        12,
        8,
        15,
        13,
        18,
        12,
        28,
        14,
        24,
        24,
        31,
        18,
        39,
        20,
        42,
    ]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A000203(start, limit)) == limit
