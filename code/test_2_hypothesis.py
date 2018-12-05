"""Tests using correct functions.
"""
from hypothesis import given
from hypothesis.strategies import integers, floats

from base_functions import correct_product_integers


@given(x=integers(), y=floats(allow_nan=False, allow_infinity=False))
def test_product_of_integers(x: int, y: int) -> int:
    """Testsd the result is x times y.
    """
    print(x, y)
    result = correct_product_integers(x, y)
    assert result == x * y
