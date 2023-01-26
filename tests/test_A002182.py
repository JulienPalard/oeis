from oeis import A002182


def test_A002182():
    from_oeis_org = [
        int(i)
        for i in """1 2 4 6 12 24 36 48 60 120 180 240 360 720 840 1260
        1680 2520 5040 7560""".split()
    ]
    assert A002182[1 : len(from_oeis_org) + 1] == from_oeis_org
