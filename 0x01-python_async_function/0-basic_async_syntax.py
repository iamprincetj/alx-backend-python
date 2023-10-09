#!/usr/bin/env python3
'''Module for using the basics of async syntax'''
import asyncio
import random

async def wait_random(max_delay=10):
    ran_num = random.uniform(0, max_delay)
    await asyncio.sleep(ran_num)
    return ran_num


print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))