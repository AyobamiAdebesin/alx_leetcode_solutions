#!/usr/bin/python3
def solution(sequence):
    for i in range(len(sequence)):
        new_arr = sequence[:i] + sequence[i+1:]
        if new_arr == list(sorted(new_arr)) and len(set(new_arr)) == len(new_arr):
            return True
    return False
# def solution(sequence):
#     for i in range(len(sequence)):
#         print(f"Starting {i}th loop....... ")
#         new_arr = sequence[:]
#         elem = new_arr[i]
#         new_arr.remove(elem)
#         # print(f"Original array: {new_arr}")
#         # print(f" Sorted array: {sorted(new_arr)}")
#         # print(f"Removing element::: {elem}")
#         if new_arr == sorted(new_arr):
#             return True
#     return False

if __name__ == "__main__":
    #arr = [1,2,3,4,3,6]
    arr = [1, 2, 1, 2]
    print(solution(arr))
