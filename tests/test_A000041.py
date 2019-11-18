from oeis import partitions
def test_partitions():
    assert partitions(5)==7
    assert partitions(3)==3
    assert partitions(4)==5
    assert partitions(10)==42