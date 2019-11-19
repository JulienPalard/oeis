from oeis import A001247


def testA001247():
    test = A001247(3, 20)
    assert 1 in test
    assert 4 in test
    assert 25 in test
    assert 225 in test
