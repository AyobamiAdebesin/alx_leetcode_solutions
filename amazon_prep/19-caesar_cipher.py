#!/usr/bin/python3
""" Caesar's Cipher """

def caesar_cipher(s, k):
    # Write your code here
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for char in s:
        if char.isalpha():
            if char == char.lower():
                idx = alphabets.index(str(char))
                new_string += alphabets[(idx + k) % len(alphabets)]
            else:
                char = char.lower()
                idx = alphabets.index(str(char))
                new_string += alphabets[(idx + k) % len(alphabets)].upper()
        else:
            new_string += char
    return new_string


if __name__ == "__main__":
    print(caesar_cipher("middle-Outz", 2))