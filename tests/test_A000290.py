from oeis import A000290


def test_squares():
    assert A000290[:6] == [0, 1, 4, 9, 16, 25]
