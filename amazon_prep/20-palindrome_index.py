#!/usr/bin/python3
def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if s[left+1:right+1] == s[left+1:right+1][::-1]:
                return left
            else:
                return right
        left += 1
        right -= 1

    return -1

if __name__ == "__main__":
    print(palindromeIndex("ayobami"))  # Output: 1
    p = 12345
    sum_ = sum(int(x) for x in str(p))
