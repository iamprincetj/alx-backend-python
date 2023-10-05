#!/usr/bin/env python3

'''Basic annotations - floor'''
import math

def floor(n: float) -> int:
    '''Returns the floor of the float'''
    return int(n // 1)
ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))