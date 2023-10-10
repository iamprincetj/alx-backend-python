#!/usr/bin/env python3
""" A Module That Implements Async Generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ A Function That Generates Random Numbers From 0 to 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
