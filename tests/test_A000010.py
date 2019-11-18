from oeis import phi

def test_phi():
    assert [phi(x) for x in range (1, 10)] == [1, 1, 2, 2, 4, 2, 6, 4, 6]