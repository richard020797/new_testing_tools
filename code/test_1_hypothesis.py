"""Tests using hypothesis that do not work.
"""
from hypothesis import given
from hypothesis.strategies import integers, lists

from base_functions import product_integers


def test_product_of_integers():
    """Tests the result is x times y.
    """
    test_cases = ((0, 0), (10000, 0), (2, 3), (-10, -13), (4, -6))
    for a, b in test_cases:
        result = product_integers(a, b)
        assert result == a * b

@given(x=integers(), y=integers())
def test_product_of_integers_2(x: int, y: int) -> int:
    """Tests the result is x times y.
    """
    print(x, y)
    result = product_integers(x, y)
    assert result == x * y
