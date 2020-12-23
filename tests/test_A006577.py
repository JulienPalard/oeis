from oeis import A006577


def test_A006577():
    expected = "0 1 7 2 5 8 16 3 19 6 14 9 9 17 17 4 12 20 20 7 7 15 15 10 23".split()
    expected = [int(e) for e in expected]
    assert A006577[1 : len(expected) + 1] == expected
