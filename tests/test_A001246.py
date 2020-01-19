from oeis import A001246


def test_catalan():
    assert A001246[:10] == [
        1,
        1,
        4,
        25,
        196,
        1764,
        17424,
        184041,
        2044900,
        23639044,
    ]
