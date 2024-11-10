#!/usr/bin/env python3
"""
Module containing the `make_multiplier` function that takes a float `multiplier`
and returns a function that multiplies a given float by the multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by a constant multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float `x` and returns
        the product of `x` and `multiplier`.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
