#!/usr/bin/python3

"""
Complete the 'matchStrings' function below.

The function is expected to return a STRING_ARRAY.
The function accepts following parameters:
 1. STRING_ARRAY text
 2. STRING_ARRAY pat


Construct a function, matchStrings, that matches patterns in pat with strings in text.
The pattern is a string with a wildcard character '*'.
The function should match the part before '*' and the part after '*'
with the beginning and the end of the string, respectively.

"""

import math
import os
import random
import sys

# Initial solution but only 2/15 test cases passed.
def matchStrings(text, pat):
    # Write your code here
    output = [''] * len(text)
    for i in range(len(text)):
        strng = text[i]
        the_pat = pat[i]
        idx = the_pat.index('*')
        part1 = the_pat[0:idx]
        part2 = the_pat[idx+1:]
        len_part1 = len(part1)
        part1_text = strng[0:len_part1]
        part2_text = strng[len(strng) - len_part2:]
        # pat_len = len(the_pat)
        if part1_text == part1 and part2_text == part2:
            output[i] += 'YES'
        elif part1 == '' and part2_text == part2:
            output[i] += 'YES'
        elif part2 == '' and part1_text == part1:
            output[i] += 'YES'
        # if part1 in string
        # elif part1 in strng and part2 not in strng:
        #     output[i] += 'NO'
        # elif part1 not in strng and part2 in strng:
        #     output[i] += 'NO'
        else:
            output[i] += 'NO'
    return output

# Correct solution
def matchStrings(text, pat):
    output = [''] * len(text)
    for i in range(len(text)):
        strng = text[i]
        the_pat = pat[i]
        if '*' in the_pat:
            idx = the_pat.index('*')
            part1 = the_pat[0:idx]
            part2 = the_pat[idx+1:]
            len_part1 = len(part1)
            len_part2 = len(part2)
            part1_text = strng[0:len_part1]
            part2_text = strng[len(strng) - len_part2:]
            if part1 == part1_text and part2 == part2_text:
                output[i] = "YES"
            else:
                output[i] = "NO"
        else:
            if the_pat == strng:
                output[i] = "YES"
            else:
                output[i] = "NO"
    return output
