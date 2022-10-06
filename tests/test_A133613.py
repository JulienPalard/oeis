import re
from math import floor

from hypothesis import given
from hypothesis.strategies import integers

from oeis import A133613, A183613

FROM_OEIS = """7, 8, 3, 5, 9, 1, 4, 6, 4, 2, 6, 2, 7, 2, 6, 5, 7, 5, 4, 0, 1, 9, 5, 0,
9, 3, 4, 6, 8, 1, 5, 8, 4, 8, 1, 0, 7, 6, 9, 3, 2, 7, 8, 4, 3, 2, 2, 2, 3, 0, 0, 8, 3,
6, 6, 9, 4, 5, 0, 9, 7, 6, 9, 3, 9, 9, 8, 1, 6, 9, 9, 3, 6, 9, 7, 5, 3, 5, 2, 6, 5, 1,
5, 8, 3, 9, 1, 8, 1, 0, 5, 6, 2, 8, 4, 2, 4, 0, 4, 9, 8, 0, 5, 1, 6"""


def test_A133613():
    expected = [int(x) for x in re.findall("[0-9]+", FROM_OEIS)]
    assert A133613[: len(expected)] == expected


@given(integers(min_value=1, max_value=100))
def test_A133613_formula(n):
    """Tests the formula:

    a(n) = floor( A183613(n+1) / 10^n )
    """
    assert A133613[n] == floor(A183613[n + 1] / 10**n)
