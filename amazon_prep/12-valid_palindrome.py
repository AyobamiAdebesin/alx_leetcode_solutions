#!/usr/bin/python3
"""
Given a string s, check if 
the string is a valid palindrome
"""
from math import inf
def valid_palindrome(s):
    i = 0
    j = len(s) - 1
    while (i < j):
        while not str(s[j]).isalnum():
            j -= 1
        while not str(s[i]).isalnum():
            i += 1
        if str(s[i]).lower() != str(s[j]).lower():
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(valid_palindrome(s))
