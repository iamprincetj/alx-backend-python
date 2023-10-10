#!/usr/bin/env python3
""" A Module That Implements Async Comprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ A Function That Returns A List Of 10 Random Numbers """
    return [i async for i in async_generator()]
