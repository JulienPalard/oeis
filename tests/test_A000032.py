from oeis import A000032


def test_A000032():
    assert A000032[:11] == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
