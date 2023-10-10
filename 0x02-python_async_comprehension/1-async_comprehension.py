#!/usr/bin/env python3
""" A Module That Implements Async Comprehensions """
async_generator = __import__('0-async_generator').async_generator
from typing import List, Generator

async def async_comprehension():
    """ A Function That Returns A List Of 10 Random Numbers """
    return [i async for i in async_generator()]
