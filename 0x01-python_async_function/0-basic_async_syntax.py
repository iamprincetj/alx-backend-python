#!/usr/bin/env python3
'''Module for using the basics of async syntax'''
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    '''Asynchronous coroutine that takes in an integer argument'''
    ran_num = random.uniform(0, max_delay)
    await asyncio.sleep(ran_num)
    return ran_num
