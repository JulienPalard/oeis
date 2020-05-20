from hypothesis import given
from hypothesis.strategies import integers

from oeis import A000045


@given(integers(min_value=2, max_value=1000))
def test_A000045(i):
    assert A000045[i] == A000045[i - 1] + A000045[i - 2]


def test_A000045_start():
    """I personally prefer fib to start with (1, 1) as it's originally a
    study of rabbit population, which cannot bootstrap itself with 0
    rabbits.

    But the OEIS is explicit about A000045 starting by 0: "with F(0) = 0".
    """
    assert A000045[:2] == [0, 1]
