#!/usr/bin/env python3
""" A Module That Implements Async Generator """
import random
import asyncio


async def async_generator():
    """ A Function That Generates Random Numbers From 0 to 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)