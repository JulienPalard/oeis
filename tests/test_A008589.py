from oeis import A008589
from hypothesis import given
from hypothesis.strategies import integers


def test_A008589_start():
    test = A008589[:40]
    assert 7 in test
    assert 14 in test
    assert 21 in test
    assert 28 in test


@given(integers(min_value=0))
def test_A008589(i):
    assert A008589[i] % 7 == 0
