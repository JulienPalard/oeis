from oeis import fibonacci
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=17))
def test_A000045(x):
    assert fibonacci(x)
