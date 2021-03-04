from oeis import A000119


def test_sequence():
    assert A000119[:10] == [
        1,
        1,
        1,
        2,
        1,
        2,
        2,
        1,
        3,
        2,
    ]
