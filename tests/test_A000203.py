from oeis import A000203


def test_sequence():
    from_oeis_org = [
        int(i)
        for i in """1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36
        24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124
        57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144
        """.split()
    ]
    assert A000203[1 : len(from_oeis_org) + 1] == from_oeis_org
