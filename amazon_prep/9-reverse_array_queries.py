#!/usr/bin/python3
""" Perform certain operations on an array """

def performOperations(arr: List, operations):
    init_arr = arr
    unsorted_arr = arr
    for op in operations:
        i, j = op[0,1]
        sub_array = arr[i:j+1]
        sub_array.reverse()
        arr[i:j+1] = sub_array
    return arr 