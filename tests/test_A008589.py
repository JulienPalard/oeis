from oeis import A008589


def testA008589():
    test = A008589(3, 40)
    assert 7 in test
    assert 14 in test
    assert 21 in test
    assert 28 in test
