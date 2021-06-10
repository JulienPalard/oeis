from oeis import A008587
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=0))
def test_divisible_by_five(n):
    assert A008587[n] % 5 == 0


def test_A008587():
    test = A008587[:30]
    assert 5 in test
    assert 10 in test
    assert 15 in test
    assert 20 in test
