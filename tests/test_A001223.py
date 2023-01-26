from oeis import A001223


def test_A001223():
    from_oeis_org = [
        int(i)
        for i in """1 2 2 4 2 4 2 4 6 2 6 4 2 4 6 6 2 6 4 2 6 4 6 8
        4 2 4 2 4 14 4 6 2 10 2 6 6 4 6 6 2 10 2 4 2 12 12 4 2 4 6 2 10 6 6
        6 2 6 4 2 10 14 4 2 4 14 6 10 2 4 6 8 6 6 4 6 8 4 8 10 2 10 2 6 4 6
        8 4 2 4 12 8 4 8 4 6 12 """.split()
    ]
    assert A001223[1 : len(from_oeis_org) + 1] == from_oeis_org
