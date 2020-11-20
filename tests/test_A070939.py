from oeis import A070939


def test_sequence():
    assert A070939[:10] == [
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        4,
        4,
    ]
