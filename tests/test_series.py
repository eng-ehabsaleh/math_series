
from math_series.series import fibonacci


def test_fibonacci():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


# def test_lucas():
#     actual = lucas(9)
#     expected = 76
#     assert actual == expected