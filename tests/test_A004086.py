import random

from oeis import A004086
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=10000))
def test_sequence(n):
    assert A004086[A004086[n]] == int(str(n).rstrip("0"))


def test_sequence_other_values():
    for i in range(100):
        result = random.choices("123456789", k=5)
        assert A004086[int("".join(result))] == int("".join(reversed(result)))
