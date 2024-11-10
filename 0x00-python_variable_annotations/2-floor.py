#!/usr/bin/env python3
"""
Basic annotations - floor function.

This module defines a type-annotated function `floor` that takes a float `n`
as an argument and returns the largest integer less than or equal to `n`.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The float value to floor.

    Returns:
        int: The largest integer less than or equal to `n`.
    """
    return math.floor(n)
