from math import floor, sqrt

from hypothesis import given
from hypothesis.strategies import integers

from oeis import A000037


def first_formula(n):
    return n + floor(1 / 2 + sqrt(n))


@given(integers(min_value=1))
def test_first_formula(n):
    assert first_formula(n) == A000037[n]


# To uncomment when we have an implementation for A000194
# @given(integers(min_value=1))
# def test_last_formula(n):
#     assert A000037[n] == A000194[n] + n


# To uncomment when we have an implementation for A010052
# @given(integers(min_value=1))
# def test_reinhard_zumkeller(n):
#     """A010052(a(n)) = 0. - Reinhard Zumkeller, Jan 26 2010."""
#     assert A010052[A000037[n]] == 0


def test_no_squares():
    """For example note that the squares 0, 1, 4, 9, 16 are not included."""
    assert {0, 1, 4, 9, 16} & set(A000037[1:17]) == set()
