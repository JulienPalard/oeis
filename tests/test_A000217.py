from oeis import A000217


def test_sequence():
    assert A000217() == [
        0,
        1,
        3,
        6,
        10,
        15,
        21,
        28,
        36,
        45,
        55,
        66,
        78,
        91,
        105,
        120,
        136,
        153,
        171,
        190,
    ]
