#!/usr/bin/env python3
'''Module for using the basics of async syntax imports wait_random
   from the previous python file'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''Asynchronous coroutine that takes in an integer argument
       (max_delay, with a default value of 10) named wait_random
       that waits for a random delay between 0 and max_delay
       (included and float value) seconds and eventually returns it.'''
    list_of_delays = []
    for i in range(n):
        func = await wait_random(max_delay)
        list_of_delays.append(func)
    return sorted(list_of_delays)
