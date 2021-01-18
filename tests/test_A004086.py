from oeis import A004086
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=10000))
def test_sequence(n):
    assert A004086[A004086[n]] == int(str(n).rstrip("0"))


@given(integers(min_value=100000000, max_value=999999999))
def test_sequence_other_values(n):
    assert A004086[n] == int("".join(reversed(str(n))))
