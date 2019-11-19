from oeis import A001220


def test_A001220():
    assert A001220(0, 3000, False) == [1, 1093]
