#!/usr/bin/python3
"""
Given an array of integers, calculate the 
ratios of its elements that are positive, 
negative, and zero. Print the decimal value
of each fraction on a new line with 
places after the decimal.
"""

def plusMinus(arr):
    # Write your code here
    zero_cnt = 0
    pos_cnt = 0
    neg_cnt = 0
    for x in arr:
        if x > 0:
            pos_cnt+=1
        elif x < 0:
            neg_cnt+=1
        elif x == 0:
            zero_cnt+=1
        pos_ratio = 0.0
    neg_ratio = neg_cnt/len(arr)
    zero_ratio = zero_cnt/len(arr)
    pos_ratio = pos_cnt/len(arr)
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == "__main__":
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)