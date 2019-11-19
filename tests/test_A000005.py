from oeis import A000005
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000005() == [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A000005(start, limit)) == limit
