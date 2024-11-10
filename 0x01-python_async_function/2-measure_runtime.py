#!/usr/bin/env python3
"""
Module to measure the runtime of the `wait_n` coroutine.
"""

import asyncio
import time

def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure the average runtime of the `wait_n` coroutine over
    `n` iterations.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay time for each coroutine.

    Returns:
        float: Average execution time of `wait_n` over `n` iterations.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    
    # Run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))

    # Return the average time per execution
    return (time.time() - start_time) / n
