from oeis import A000041


def test_partitions():
    assert A000041(0, 10) == [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
