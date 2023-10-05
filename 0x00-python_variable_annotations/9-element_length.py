#!/usr/bin/env python3
'''Module that takes a list and returns a tuple with its length'''

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a tuple with its length'''
    return [(i, len(i)) for i in lst]
