from oeis import A000142
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A000142() == [
        1,
        1,
        2,
        6,
        24,
        120,
        720,
        5040,
        40320,
        362880,
        3628800,
        39916800,
        479001600,
        6227020800,
        87178291200,
        1307674368000,
        20922789888000,
        355687428096000,
        6402373705728000,
        121645100408832000,
    ]


@given(integers(min_value=0, max_value=20), integers(min_value=1, max_value=20))
def test_sequence_length(x, y):
    assert len(A000142(x, y)) == y
