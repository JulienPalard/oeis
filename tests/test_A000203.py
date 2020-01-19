from oeis import A000203


def test_sequence():
    assert A000203[:20] == [
        1,
        3,
        4,
        7,
        6,
        12,
        8,
        15,
        13,
        18,
        12,
        28,
        14,
        24,
        24,
        31,
        18,
        39,
        20,
        42,
    ]
