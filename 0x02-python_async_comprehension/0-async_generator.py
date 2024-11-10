#!/usr/bin/env python3
"""
Module containing an asynchronous coroutine called async_generator
that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates 10 random numbers between 0 and 10,
    with a 1-second delay between each generation.

    Returns:
        A generator yielding random floats between 0 and 10.
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)

        # Generate a random number between 0 and 10
        yield random.random() * 10
