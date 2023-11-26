#!/usr/bin/python3

"""
Given a string find the length
of the longest substring without repeating
characters
"""

def find_longest_substring(s) -> int:
    start = 0
    max_length = 0
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index and start <= char_index[s[end]]:
            start = char_index[s[end]] + 1
        else:
            max_length = max(max_length, end - start +1)
        char_index[s[end]] = end
    return max_length



if __name__ == "__main__":
    s = "ayobbami"
    print(find_longest_substring(s))