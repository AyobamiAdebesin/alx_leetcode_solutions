#!/usr/bin/python3

def solution(s):
    duplicate_arr = {}
    seen = set()
    count = 0
    for i in range(len(s)):
        if s[i] in seen:
            duplicate_arr[s[i]] += 1
        else:
            duplicate_arr[s[i]] = 1
            seen.add(s[i])
    for char in s:
        if duplicate_arr[char] == 1:
            return char
    else:
        return '_'

if __name__ == "__main__":
    s = "abacabad"
    print(solution(s))