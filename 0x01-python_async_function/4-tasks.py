#!/usr/bin/env python3
'''Module for using the basics of async syntax  alters wait_n'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''A function that takes in an integer arguments and
       calls task_wait_random n times'''
    myList = []
    for _ in range(n):
        func = task_wait_random(max_delay)
        myList.append(func)
    return [await task for task in asyncio.as_completed(myList)]
