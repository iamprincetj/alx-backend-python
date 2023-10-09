#!/usr/bin/env python3
'''Module for using the basics of async syntax imports wait_n'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Asynchronous coroutine that measures the total execution time
        for wait_n(n, max_delay), and returns total_time / n'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
