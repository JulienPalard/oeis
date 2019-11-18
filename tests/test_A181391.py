from oeis import A181391
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A181391() == [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3]


@given(integers(min_value=0, max_value=20000), integers(min_value=1, max_value=20000))
def test_sequence_length(x, y):
    assert len(A181391(x, y)) == y
