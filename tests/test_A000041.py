<<<<<<< HEAD
from oeis import partitions


def test_partitions():
    assert partitions(5) == 7
    assert partitions(3) == 3
    assert partitions(4) == 5
    assert partitions(10) == 42
=======
from oeis import A000041


def test_partitions():
    assert A000041(5) == 7
    assert A000041(3) == 3
    assert A000041(4) == 5
    assert A000041(10) == 42

>>>>>>> 0a6bf138ef7ffc250bfdb878f718a052df4da8f9
