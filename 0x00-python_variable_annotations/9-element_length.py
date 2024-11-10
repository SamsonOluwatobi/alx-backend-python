#!/usr/bin/env python3
"""
Module containing a function that annotates the parameters and return types
appropriately for a function that processes sequences.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing a sequence from the input
    iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., list of strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
