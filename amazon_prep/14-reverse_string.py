#!/usr/bin/python3
"""
Given an input string, reverse
the string word by word
"""

def reverse_string(s: str):
    word_list = s.split(" ")
    word_list.reverse()
    new_s = ""
    for word in word_list:
        new_s += f" {word}"
    print(new_s)

if __name__ == "__main__":
    s = "the sky is blue"
    reverse_string(s)

"a".index(0)