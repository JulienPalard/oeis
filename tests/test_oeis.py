import pytest
from itertools import product
from oeis import oeis, A001220


@pytest.mark.parametrize(
    "serie,start,stop",
    product(oeis.series.values(), list(range(4)), list(range(2, 6))),
)
def test_semantics(serie, start, stop):
    """Test the semantics are the same as the range builtin function."""
    if serie == A001220:
        pytest.skip("Way too long to test A001220 with more than 2 elements.")
    assert len(range(stop)) == len(serie[:stop])
    assert len(range(start, stop)) == len(serie[start:stop])


def test_stop_iteration():
    assert A001220[0]
    assert A001220[1]
    with pytest.raises(IndexError):
        A001220[2]


def test_iteration():
    for i in A001220:
        assert i


def test_negative_index():
    with pytest.raises(ValueError):
        A001220[-1]
    with pytest.raises(ValueError):
        A001220[-1:]


def test_get_by_name():
    oeis["A001220"][0] == A001220[0]
