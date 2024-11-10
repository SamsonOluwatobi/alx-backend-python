#!/usr/bin/env python3
"""
Task 4: Execute multiple asynchronous tasks and return sorted delay times.
"""

import asyncio
from typing import List

# Import the task_wait_random function from 3-tasks
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times and returns the delays sorted in
    ascending order.

    Args:
        n (int): Number of times to execute the task.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Sorted list of delay times.
    """
    # Create a list of delay times by awaiting the task n times
    wait_times = [await task_wait_random(max_delay) for _ in range(n)]

    # Return the sorted list of delay times
    return sorted(wait_times)
