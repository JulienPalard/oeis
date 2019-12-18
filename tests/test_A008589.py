from oeis import A008589
from hypothesis import given
from hypothesis.strategies import integers


@given(integers())
def test_A008589(start):
    test = A008589(3, 40)
    assert 7 in test
    assert 14 in test
    assert 21 in test
    assert 28 in test
    assert A008589(start, 1)[0] % 7 == 0
