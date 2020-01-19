from hypothesis import given
from hypothesis.strategies import integers

from oeis import A000045


@given(integers(min_value=2, max_value=1000))
def test_A000045(i):
    assert A000045[i] == A000045[i - 1] + A000045[i - 2]


def test_A000045_start():
    assert A000045[:2] == [1, 1]
