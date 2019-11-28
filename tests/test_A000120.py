from oeis import A000120
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000120() == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A000108(start, limit)) == limit
