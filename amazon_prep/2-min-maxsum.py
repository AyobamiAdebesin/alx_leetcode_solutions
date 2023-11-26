#!/bin/python3
"""
Given five positive integers, find
the minimum and maximum values that
can be calculated by summing exactly
four of the five integers. Then print
the respective minimum and maximum values 
as a single line of two space-separated
long integers
"""
import math
import os
import random
import re
import copy
import sys



def miniMaxSum(arr):
    # Write your code here
    arr_copy = copy.deepcopy(arr)
    max_no = max(arr_copy)
    min_no = min(arr_copy)
    arr_copy.remove(min_no)
    arr.remove(max_no)
    max_sum = sum(arr_copy)
    min_sum = sum(arr)
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)