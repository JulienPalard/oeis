from oeis import A001969
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A001969[:10] == [
        0,
        3,
        5,
        6,
        9,
        10,
        12,
        15,
        18,
        20,
    ]
