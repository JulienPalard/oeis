from oeis import A000290


assert [A000290(i) for i in range(6)] == [1, 4, 9, 16, 25, 36]


def test_A000290():
    assert A000290(start=0, limit=7) == [0, 1, 4, 9, 16, 25, 36]
