#!/usr/bin/python3
"""
Given an array of integers, where all elements
but one ocur twice. Find the unique element"""

import os
import sys
import time

def lonelyinteger(a):
    # Write your code here
    # dict_arr = {}
    # for x in a:
    #     if str(x) in dict_arr.keys():
    #         dict_arr[str(x)] += 1
    #     else:
    #         dict_arr[str(x)] = 1
    # dict_keys = list(dict_arr.keys())
    # dict_values = list(dict_arr.values())
    # min_val = min(list(dict_values))
    # pos = dict_values.index(min_val)
    # return (dict_keys[pos])
    for x in a:
        if a.count(x) == 1:
            return x

if __name__ == "__main__":
    print(lonelyinteger([1,2,3,4,3,2,1]))