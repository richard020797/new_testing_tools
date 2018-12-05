"""The base  used in the tests examples.
"""
from dpcontracts import require, ensure

options = {
    '0': 0,
    '10000': 0,
    '2': 6,
    '-10': 130,
    '4': -24
}


def product_integers(x: int, y: int) -> int:
    """Custom Product of two int numbers.
    """
    return options.get(str(x), 0)


def correct_product_integers(x: int, y: int) -> int:
    """Product of two int munbers.
    """
    return x * y


@require("x and y must be integers.",
    lambda args: isinstance(args.x, int) and isinstance(args.y, int))
@ensure("The return value is an integer.",
    lambda args, result: isinstance(result, int))
def typed_checked_product_integers(x: int, y: int) -> int:
    """The product of two int numbers checked by type.
    """
    return x * y
