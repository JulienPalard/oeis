from oeis import A002275


def test_A002275():
    assert A002275(start=0, limit=7) == [0, 1, 11, 111, 1111, 11111, 111111]