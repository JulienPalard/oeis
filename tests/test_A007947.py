from functools import reduce

from hypothesis import given, settings
from hypothesis.strategies import integers

from oeis import A000040, A007947


def test_sequence():
    assert A007947[1:21] == [
        1,
        2,
        3,
        2,
        5,
        6,
        7,
        2,
        3,
        10,
        11,
        6,
        13,
        14,
        15,
        2,
        17,
        6,
        19,
        10,
    ]


@given(integers(min_value=1, max_value=100), integers(min_value=1, max_value=100))
@settings(deadline=None)
def test_A007947(start, stop):
    composite = reduce(lambda x, y: x * y, A000040[start : start + stop], 1)
    expected = reduce(lambda x, y: x * y, set(A000040[start : start + stop]), 1)
    assert A007947[composite] == expected
