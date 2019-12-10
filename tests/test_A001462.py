from oeis import A001462

def test_A001462():
    assert A001462(start=1, limit=10) == [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
    assert A001462(start=1, limit=1)[0] == 1
    assert A001462(start=2, limit=1)[0] == 2