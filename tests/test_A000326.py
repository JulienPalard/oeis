from oeis import A000326


def test_pentagonal():
    assert A000326[:10] == [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]
