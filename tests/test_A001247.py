from oeis import A001247


def test_A001247():
    assert A001247(limit=10) == [
        1,
        1,
        4,
        25,
        225,
        2704,
        41209,
        769129,
        17139600,
        447195609,
    ]