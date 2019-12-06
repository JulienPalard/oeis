from hypothesis import given
from hypothesis.strategies import integers

from oeis import A000045


def fib(x):
    return A000045(x, limit=1)[0]


@given(integers(min_value=2, max_value=1000))
def test_A000045(i):
    assert fib(i) == fib(i - 1) + fib(i - 2)
    assert A000045(limit=2) == [1, 1]
