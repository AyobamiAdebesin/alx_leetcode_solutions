#!/usr/bin/python3
""" Counting sort"""

def countingSort(arr):
    """ Counting sort """
    frequency = [0] * 100
    for value in arr:
        frequency[value] += 1
    return frequency


if __name__ == "__main__":
    arr = [1, 1, 3, 2, 1]
    print(countingSort(arr))

    min_val = min(arr)
    max_val = max(arr) + 1

    zero_arr = []
    for i in range(min_val, max_val+1):
        zero_arr.append(0)
    for x in arr:
        zero_arr[x] += 1
    return zero_arr