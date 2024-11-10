#!/usr/bin/env python3
"""
Type-annotated function `sum_list` that takes a list of floats
as an argument and returns their sum as a float.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all elements in `input_list`.
    """
    sum_val = 0.0
    for i in input_list:
        sum_val += i

    return sum_val
