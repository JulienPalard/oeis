from oeis import A001969


def test_sequence():
    assert A001969[:10] == [
        0,
        3,
        5,
        6,
        9,
        10,
        12,
        15,
        17,
        18,
    ]
