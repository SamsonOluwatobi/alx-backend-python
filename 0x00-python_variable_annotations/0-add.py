#!/usr/bin/env python3
"""
Basic annotations - add function.

This module defines a type-annotated function `add` that takes two floats,
`a` and `b`, as arguments and returns their sum as a float.
"""

def add(a: float, b: float) -> float:
    """
    Returns the sum of two float arguments.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b
