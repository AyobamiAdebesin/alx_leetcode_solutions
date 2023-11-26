#!/usr/bin/python3
""" Check if a string of bracket is balanced """

def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if len(stack) == 0 or bracket_map[char] != stack.pop():
                return 'NO'
        else:
            return 'NO'
    return 'YES' if len(stack) == 0 else "NO"