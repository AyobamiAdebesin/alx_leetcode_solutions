#!/usr/bin/python3

def solution(s: str):
    while len(s) > 1:
        prefix = longest_palindrome_prefix(s)
        if len(prefix) >= 2:
            s = s.replace(prefix, "", 1)
        else:
            break
    return s

def valid_palindrome(s):
    i = 0
    j = len(s) -1
    while (i < j):
        while not str(s[j]).isalnum():
            j -= 1
        while not str(s[i]).isalnum():
            i += 1
        if str(s[i]).lower() != str(s[j]).lower():
            return False
        i+=1
        j-=1
    return True

def longest_palindrome_prefix(s):
    n = len(s)
    longest_prefix = ""
    for i in range(n):
        prefix = s[0: i+1]
        if valid_palindrome(prefix) and len(prefix) > len (longest_prefix):
            longest_prefix = prefix
    return longest_prefix


# def solution(s: str):
#     prefix_list = []
#     palindrome_maps = {}
#     if len(s) == 1:
#         return s
#         for i in range(len(s)):
#             prefix_list.append(s[0: i+1])
#         for prefix in prefix_list:
#             if isPalindrome(prefix) == True:
#                 palindrome_maps[len(prefix)] = prefix
#         if palindrome_maps == {}:
#             return s
#         else:
#             longest_palindrome = max(palindrome_maps.keys())
#             if longest_palindrome >= 2:
#                 if longest_palindrome == len(s):
#                     return ""
#                 else:
#                     s = s.replace(prefix, " " , 1)
#     return s
        
# def valid_palindrome(s):
#     i = 0
#     j = len(s) -1
#     while (i < j):
#         while not str(s[j]).isalnum():
#             j -= 1
#         while not str(s[i]).isalnum():
#             i += 1
#         if str(s[i]).lower() != str(s[j]).lower():
#             return False
#         i+=1
#         j-=1
#     return True
    