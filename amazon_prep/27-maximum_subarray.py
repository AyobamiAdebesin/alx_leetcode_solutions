#!/usr/bin/python3
def maximum_subarray(nums):
    """ Find the subarray with the largest sum and return its sum"""
    max_sum = current_sum = nums[0]

    print(f"current sum before loop: {current_sum}")
    print(f"maximum sum before loop: {max_sum}\n")

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        print(f"current sum: {current_sum}")
        max_sum = max(max_sum, current_sum)
        print(f"maximum sum: {max_sum}\n")

    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximum_subarray(nums))