#!/usr/bin/env/python3
"""Module that takes a list input_list of mixed integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float."""
    return sum(mxd_lst)
