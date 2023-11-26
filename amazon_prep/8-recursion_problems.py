#!/usr/bin/python3
""" Compute power of 2 """

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

def powerofTwo(n):
    if n == 0:
        return 1
    else:
        return 2* power(n-1)

def factorial(n):
    if n>=1 and isinstance(n, int):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return 0

def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[-1]:
        return False
    else:
        return isPalindrome(strng[1:-1])

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


def reverseString(s):
    new_s = ''
    if len(s) == 1:
        return s
    else:
        new_s+=s[-1]
        return new_s + reverseString(s[0:len(s)-1])
        

if __name__ == "__main__":
    print(reverseString("string"))