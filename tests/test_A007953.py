from oeis import A007953


def test_sequence():
    assert A007953() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert A007953(20, 10) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
