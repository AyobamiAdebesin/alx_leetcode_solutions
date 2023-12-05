#!/usr/bin/python3
"""
Implement a custom hash map
that supports the following operations:
insert, addToKey, addToValue, get

Return the sum of all the get values
"""

def solution(queryType, query):
    hash_map = {}
    output = 0
    for que, arg in zip(queryType, query):
        if que == 'insert':
            hash_map[arg[0]] = arg[1]
        elif que == 'addToValue':
            if len(hash_map) != 0:
                hash_map = {key: value + arg[0] for key, value in hash_map.items()}
            else:
                continue
        if que == 'addToKey':
            if len(hash_map) != 0:
                hash_map = {key + arg[0]: value for key, value in hash_map.items()}
            else:
                continue
        if que == 'get':
            if len(hash_map) != 0:
                output += hash_map[arg[0]]
            else:
                continue
    return output

        

