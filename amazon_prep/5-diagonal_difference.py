#!/usr/bin/python3
"""
Given a square matrix, calculate
the absolute difference between
the sums of its diagonals.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diag = 0
    right_diag = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                left_diag += arr[i][j]
            if i+j == len(arr) -1:
                right_diag += arr[i][j]
    diff = abs(left_diag - right_diag)
    return int(diff)
