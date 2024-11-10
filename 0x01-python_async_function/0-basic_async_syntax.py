#!/usr/bin/env python3
"""
Module containing an asynchronous coroutine `wait_random` that takes an 
integer argument `max_delay` (with a default value of 10) and waits for 
a random delay between 0 and `max_delay` seconds, eventually returning 
the delay as a float.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and 
    `max_delay` (inclusive) seconds and returns the delay as a float.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: A random delay between 0 and `max_delay` seconds.
    """
    # Generate a random floating-point number between 0 and max_delay
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)

    return delay_time
