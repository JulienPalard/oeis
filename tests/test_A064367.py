from oeis import A064367


def test_sequence():
    assert A064367[1:21] == [
        0,
        1,
        3,
        2,
        10,
        12,
        9,
        9,
        6,
        9,
        2,
        26,
        33,
        1,
        9,
        28,
        33,
        27,
        13,
        48,
    ]
