from oeis import A000120


def test_sequence():
    assert A000120[:20] == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3]
