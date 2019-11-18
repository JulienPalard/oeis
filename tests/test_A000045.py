from oeis import Fibonacci
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value=1, max_value=20000))
def test_A000045(x):
    assert(Fibonacci(x))