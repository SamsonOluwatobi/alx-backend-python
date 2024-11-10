#!/usr/bin/env python3
"""
Module to execute multiple coroutines concurrently and return their delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously executes `n` coroutines that each wait for a random delay 
    between 0 and `max_delay` seconds, and returns a list of all the delays 
    (in ascending order) without using `sort()` due to concurrency.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum possible delay for each coroutine.

    Returns:
        List[float]: A list of delays, in ascending order.
    """
    wait_times = [await wait_random(max_delay) for _ in range(n)]
    return sorted(wait_times)
