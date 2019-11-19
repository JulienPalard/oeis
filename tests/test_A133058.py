from oeis import A133058
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A133058() == [
        1,
        1,
        4,
        8,
        2,
        8,
        4,
        12,
        3,
        1,
        12,
        24,
        2,
        16,
        8,
        24,
        3,
        21,
        7,
        27,
    ]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A133058(start, limit)) == limit
