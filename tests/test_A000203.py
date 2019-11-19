from oeis import A133058
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A133058() == [
        1,
        1,
        4,
        8,
        2,
        8,
        4,
        12,
        3,
        1,
        12,
        24,
        2,
        16,
        8,
        24,
        3,
        21,
        7,
        27,
    ]


@given(integers(min_value=0, max_value=2000), integers(min_value=1, max_value=2000))
def test_sequence_length(x, y):
    assert len(A133058(x, y)) == y
