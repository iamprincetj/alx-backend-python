#!/usr/bin/env python3
'''Module that correct duck-typed annotations'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns first element of a list'''
    if lst:
        return lst[0]
    else:
        return None
