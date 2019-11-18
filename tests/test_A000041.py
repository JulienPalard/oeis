from oeis import A000041


def test_partitions():
    assert A000041(5) == 7
    assert A000041(3) == 3
    assert A000041(4) == 5
    assert A000041(10) == 42
