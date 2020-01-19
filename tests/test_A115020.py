from oeis import A115020


def test_countdown():
    assert A115020[0:15] == [100, 93, 86, 79, 72, 65, 58, 51, 44, 37, 30, 23, 16, 9, 2]
