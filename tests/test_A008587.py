from oeis import A008587


def test_A008587():
    test = A008587(3, 30)
    assert 5 in test
    assert 10 in test
    assert 15 in test
    assert 20 in test
