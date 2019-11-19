from oeis import A000108
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000108() == [
        1,
        1,
        2,
        5,
        14,
        42,
        132,
        429,
        1430,
        4862,
        16796,
        58786,
        208012,
        742900,
        2674440,
        9694845,
        35357670,
        129644790,
        477638700,
        1767263190,
    ]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A000108(start, limit)) == limit
