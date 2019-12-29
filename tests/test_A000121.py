from oeis import A000121
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000121(0, 20) == [
        1,
        2,
        2,
        3,
        3,
        3,
        4,
        3,
        4,
        5,
        4,
        5,
        4,
        4,
        6,
        5,
        6,
        6,
        5,
        6,
    ]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A000121(start, limit)) == limit
