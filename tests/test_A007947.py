from oeis import A007947, A000040
from hypothesis import given
from hypothesis.strategies import integers
from functools import reduce


def test_sequence():
    assert A007947() == [
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


@given(integers(min_value=0, max_value=2000), integers(min_value=1, max_value=2000))
def test_sequence_length(start, limit):
    assert len(A007947(start, limit)) == limit


@given(integers(min_value=0, max_value=2000), integers(min_value=1, max_value=2000))
def test_A007947(start, limit):
    composite = reduce(lambda x, y: x * y, A000040(start, limit), 1)
    expected = reduce(lambda x, y: x * y, set(A000040(start, limit)), 1)
    assert A007947(composite, limit=1) == [expected]
