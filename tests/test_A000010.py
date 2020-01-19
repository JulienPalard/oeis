from oeis import A000010


def test_phi():
    assert A000010[1:10] == [1, 1, 2, 2, 4, 2, 6, 4, 6]
