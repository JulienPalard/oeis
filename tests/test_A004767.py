from oeis import A004767


def test_A004767():
    for value in A004767[:100]:
        assert value % 2 != 0
        assert bin(value)[-2:] == "11"
