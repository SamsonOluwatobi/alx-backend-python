#!/usr/bin/env python3
"""
Module containing the `to_kv` function, which takes a string and a number
(int or float) and returns a tuple. The tuple contains the string and the
square of the number, with the square represented as a float.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the given string and the
    second element is the square of the given number, represented as a float.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number, either integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string `k` and the square of `v`.
    """
    return (k, float(v ** 2))
