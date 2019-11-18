from oeis import A181391
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=20000))
def test_sequence_length(x):
    assert len(A181391(limit=x)) == x + 1

@given(integers(min_value=0))
def test_sequence_length(x):
    assert A181391(limit=x)
