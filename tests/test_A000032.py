from hypothesis import given
from hypothesis.strategies import integers

from oeis import A000032


def test_A000032_head():
    assert A000032[0] == 2
    assert A000032[1] == 1


@given(integers(min_value=2, max_value=1000))
def test_A000032_recurrence(n):
    assert A000032[n] == A000032[n - 1] + A000032[n - 2]


def test_A000032_first_values():
    assert A000032[:11] == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
