#!/usr/bin/python3
"""
Complete the 'getScoreDifference' function below.

The function is expected to return a LONG_INTEGER.
The function accepts INTEGER_ARRAY points as parameter.

"""

import math
import os
import random
import re
import sys

# Optimized solution
def getScoreDifference(points):
    # sort the points array in descending order
    points.sort(reverse=True)
    score_a = 0
    score_b = 0

    for i in range(len(points)):
        if i % 2 == 0:
            score_a += points[i]
        else:
            score_b += points[i]
    return abs(score_a - score_b)


# Original solution, times out with large test cases because of
# the use of max function which has a time complexity of O(n)
# making the entire code has a runtime of O(n^2)

# def getScoreDifference(points):
#     # Write your code here
#     score_a = 0
#     score_b = 0
#     count = 0
#     while len(points) != 0:
#         if count % 2 == 0:
#             max_score = max(points)
#             score_a += max_score
#             points.remove(max_score)
#             count += 1
#         elif count % 2 != 0:
#             max_score = max(points)
#             score_b += max_score
#             points.remove(score_b)
#             count += 1
#     return abs(score_a - score_b)