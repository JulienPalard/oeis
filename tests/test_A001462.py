from oeis import A001462
from functools import lru_cache
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=1000))
def test_increasing(n):
    assert A001462[n] <= A001462[n + 1]


@lru_cache(4096)
def golomb(n: int) -> int:
    """The Golomb sequence, recursive implementation."""
    if n == 1:
        return 1
    # preheat cache first
    golomb(n - 200 if n > 200 else 1)
    return 1 + golomb(n - golomb(golomb(n - 1)))


@given(integers(min_value=1, max_value=666))
def test_same_as_recursive_implem(n):
    assert golomb(n) == A001462[n]


@given(integers(min_value=1, max_value=120))
def test_consistency(n):
    assert A001462[n] == A001462[1:1820].count(n)


def test_sequence():
    values = [
        int(x)
        for x in """1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9 10 10 10
        10 10 11 11 11 11 11 12 12 12 12 12 12 13 13 13 13 13 13 14 14 14 14 14 14 15
        15 15 15 15 15 16 16 16 16 16 16 16 17 17 17 17 17 17 17 18 18 18 18 18 18 18
        19""".strip().split()
    ]
    assert A001462[1] == 1
    assert A001462[1:85] == values
