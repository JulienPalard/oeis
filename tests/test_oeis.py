import pytest
from inspect import signature
from oeis import oeis


@pytest.mark.parametrize("serie", oeis.series.values())
def test_limit(serie):
    sig = signature(serie)
    assert len(serie()) == sig.parameters["limit"].default


@pytest.mark.parametrize("serie", oeis.series.values())
def test_start(serie):
    sig = signature(serie)
    assert serie()[1:] == serie(
        start=sig.parameters["start"].default + 1,
        limit=sig.parameters["limit"].default - 1,
    )
