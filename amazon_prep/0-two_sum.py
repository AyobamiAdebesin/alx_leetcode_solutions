#!/usr/bin/python3
"""
Two sum problem:
Given an array of integers, find two numbers such
that they add up to a given number.

Return the indexes of these numbers in the array
"""

# Brute force => O(n^2), O(1)
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i+1, j+1)

# Hash table => O(n), O(n)
def two_sum_hash(arr, target):
    hash_map = {}
    for (idx, value) in enumerate(arr):
        idx = idx+1
        rem = target - value
        if rem in hash_map.keys():
            return [hash_map[rem], idx]
        else:
            hash_map[value] = idx


# Two Pointers search - If array is sorted
def two_sum_pointer(arr, target):
    i, j = 0, len(arr) -1
    while i < j:
        temp_sum = arr[i] + arr[j]
        if temp_sum < target:
            i += 1
        elif temp_sum > target:
            j -= 1
        else:
            return [i+1, j+1]


class TwoSum:
    def __init__(self):
        pass
    def add(val: int):
        if not isinstance(val, int):
            return "value must be an integer!"
    def find(value):
        pass


if __name__ == "__main__":
    print(two_sum_pointer([1,2,3,4,5,6], target=11))