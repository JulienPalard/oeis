from oeis import A000041


def test_A000041():
    assert A000041[:10] == [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
