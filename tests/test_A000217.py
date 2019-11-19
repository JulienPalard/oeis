from oeis import A000217
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000217() == [
        0,
        1,
        3,
        6,
        10,
        15,
        21,
        28,
        36,
        45,
        55,
        66,
        78,
        91,
        105,
        120,
        136,
        153,
        171,
        190,
    ]


@given(integers(min_value=0, max_value=2000), integers(min_value=1, max_value=2000))
def test_sequence_length(x, y):
    assert len(A000217(x, y)) == y
