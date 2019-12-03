from oeis import A007953
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A007953() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert A007953(20, 10) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


@given(integers(min_value=0, max_value=20000), integers(min_value=1, max_value=20000))
def test_sequence_length(start, limit):
    assert len(A007953(start, limit)) == limit
