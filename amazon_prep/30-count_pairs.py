#!/usr/bin/python3
""" Count pairs

Given an array and a target, count the number of pairs
whose difference is equal to the target
"""


def count_pairs(nums, target):
    count_dict = {}
    pair_count = 0

    for num in nums:
        complement1 = num - target
        complement2 = num + target
        if complement1 in count_dict:
            pair_count += count_dict[complement1]
        if complement2 in count_dict:
            pair_count += count_dict[complement2]
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return pair_count
