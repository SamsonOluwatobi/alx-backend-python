#!/usr/bin/env python3
"""
Module containing the async_comprehension coroutine that collects 10 random numbers
using async_generator and returns them in a list.
"""

import asyncio
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using
    an async comprehension and returns them as a list.

    Returns:
        List[float]: A list of 10 random floats generated asynchronously.
    """
    return [num async for num in async_gen()]
