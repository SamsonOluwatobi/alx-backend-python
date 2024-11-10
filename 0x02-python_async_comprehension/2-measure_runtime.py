#!/usr/bin/env python3
"""
Measure runtime for four parallel async_comprehension executions.
Execute async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
import time

# Import async_comprehension from the previous module
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to execute async_comprehension four times in parallel using
    asyncio.gather and return the total time taken.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()

    # Run async_comprehension four times concurrently
    await asyncio.gather(*(async_comp() for _ in range(4)))

    end_time = time.time() - start_time
    return end_time
