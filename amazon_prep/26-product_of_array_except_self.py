#!/usr/bin/python3
""" Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the
elements of nums except nums[i]
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1] * len(nums)
    i = 0
    j = len(nums) - 1
    while i < j:
        k = len(nums) - 1
        while k > 0:
            if k == i:
                pass
            answer[i] *= nums[k]
            k -= 1
        i += 1
    return answer

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))