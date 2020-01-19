from oeis import A000110


def test_bell():
    assert A000110[:6] == [1, 1, 2, 5, 15, 52]
