#!/usr/bin/env python3
'''Module for using the basics of async syntax imports wait_random'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Asynchronous coroutine that takes in an integer argument
       named wait_randomthat waits for a random delay
       between 0 and max_delay
       (included and float value) seconds and eventually returns it.'''
    return asyncio.create_task(wait_random(max_delay))
