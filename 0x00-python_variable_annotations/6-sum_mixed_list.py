#!/usr/bin/env python3
"""
Module containing `sum_mixed_list`, a type-annotated function that
takes a list of integers and floats and returns their sum as a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floating-point numbers.

    Returns:
        float: The sum of all elements in `mxd_lst` as a float.
    """

    return float(sum(mxd_lst))
