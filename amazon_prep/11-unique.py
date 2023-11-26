#!/usr/bin/env python3
from typing import List

def removeDuplicates(nums: List[int]):
    """ Remove duplicates """
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        # print(nums)
    return i + 1

if __name__ == "__main__":
    my_list = [1,1,2]
    print(removeDuplicates(my_list))