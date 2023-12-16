#!/usr/bin/python3

def solution(paths):
    out_str_arr = []
    out_str = []
    for i in range(len(paths)):
        paths_arr = paths[i].split('/')
        #print(paths_arr)
        for j in range(1, len(paths_arr)):
            if paths_arr[j] == "..":
                out_str.pop()
                out_str.pop()
            else:
                out_str.append(paths_arr[j])
            print(out_str)