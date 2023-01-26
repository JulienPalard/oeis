import pytest
from hypothesis import given, settings
from hypothesis.strategies import integers
from oeis import A064367


def test_sequence():
    assert A064367[1:21] == [
        0,
        1,
        3,
        2,
        10,
        12,
        9,
        9,
        6,
        9,
        2,
        26,
        33,
        1,
        9,
        28,
        33,
        27,
        13,
        48,
    ]


@settings(deadline=None)
@given(integers(min_value=1, max_value=10**5))
@pytest.mark.slow
def test_residue(i):
    """For a(n) with n <= 10^6, the following residues have not yet
    appeared: {19, 22, 46, 52, 57, 65, 70, 77, 81, 85, 88, 90, 91,
    103, 104, 106, 108, 115, 120, 122, 123, 125, ..., 15472319}
    (14537148 terms). - Michael De Vlieger, Jul 16 2017.
    """
    assert A064367[i] not in {
        19,
        22,
        46,
        52,
        57,
        65,
        70,
        77,
        81,
        85,
        88,
        90,
        91,
        103,
        104,
        106,
        108,
        115,
        120,
        122,
        123,
        125,
    }
