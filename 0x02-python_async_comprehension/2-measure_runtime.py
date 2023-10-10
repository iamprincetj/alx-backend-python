#!/usr/bin/env python3
""" A Module That Implements Measure Runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ A Function That Measures The Runtime for
        four parallel comprehensions"""
    mylist = [async_comprehension() for i in range(4)]
    start = time.time()
    await asyncio.gather(*mylist)
    return time.time() - start
