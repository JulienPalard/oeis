from oeis import A133058


def test_sequence():
    assert A133058() == [
        1,
        1,
        4,
        8,
        2,
        8,
        4,
        12,
        3,
        1,
        12,
        24,
        2,
        16,
        8,
        24,
        3,
        21,
        7,
        27,
    ]
