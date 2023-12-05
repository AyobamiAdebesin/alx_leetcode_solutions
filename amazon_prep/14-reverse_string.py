#!/usr/bin/python3
"""
Given an input string, reverse
the string word by word
"""

def reverse_words(s):
    words = s.split()
    words = words[::-1]
    reversed_s = ' '.join(words)
    return reversed_s

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(reverse_words(s))  # Output: "Panama canal: a plan, a man, A"