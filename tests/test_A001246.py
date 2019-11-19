from oeis import A001246


def test_catalan():
    test = A001246(3, 20)
    assert 1 in test
    assert 4 in test
    assert 25 in test
    assert 196 in test
