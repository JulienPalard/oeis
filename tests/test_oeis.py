import pytest
from itertools import product
from oeis import oeis, A001220, A001462


@pytest.mark.parametrize(
    "serie,start,stop",
    product(oeis.series.values(), list(range(4)), list(range(2, 6))),
)
def test_semantics(serie, start, stop):
    """Test the semantics are the same as the range builtin function."""
    if serie == A001220:
        pytest.skip("A001220 has only 2 known elements")
    assert len(range(serie.offset, stop)) == len(serie[serie.offset : stop])
    assert len(range(max(start, serie.offset), stop)) == len(
        serie[max(start, serie.offset) : stop]
    )


@pytest.mark.parametrize("serie", oeis.series.values())
def test_negative_index(serie):
    with pytest.raises(IndexError):
        serie[-1]


@pytest.mark.parametrize("serie", oeis.series.values())
def test_equivalence(serie):
    upper_bound = 10
    if serie == A001220:
        upper_bound = 1
    assert serie[serie.offset : upper_bound] == [
        serie[i] for i in range(serie.offset, upper_bound)
    ]


@pytest.mark.parametrize("serie", oeis.series.values())
def test_negative_slice(serie):
    with pytest.raises(IndexError):
        serie[-1:0]


def test_stop_iteration():
    assert A001220[1]
    assert A001220[2]
    with pytest.raises(IndexError):
        A001220[3]


def test_iteration():
    for i in A001220:
        assert i


def test_get_by_name():
    assert oeis["A001220"][1] == A001220[1]


def test_out_of_offset():
    with pytest.raises(IndexError):
        A001462[0]
    with pytest.raises(IndexError):
        A001462[0:10]


def test_mandatory_start_on_offset_different_than_zero():
    with pytest.raises(IndexError):
        A001462[:10]


def test_infinite_slice():
    with pytest.raises(IndexError):  # Not implemented yet
        A001462[1:]
