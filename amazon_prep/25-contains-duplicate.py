#!/usr/bin/python3
""" Given an integer array, return True if any
value appears at least twice in the array and
return False if every element is unique"""

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)