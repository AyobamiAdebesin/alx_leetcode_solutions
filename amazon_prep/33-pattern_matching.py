#!/usr/bin/python3
"""
You are given two strings - pattern and source. The first string pattern
contains only the symbols 0 and 1, and the second string source contains
only lowercase English letters.

Let's say that pattern matches a substring source[l..r] of source if the
following three conditions are met:

1) they have equal length,
2) for each 0 in pattern the corresponding letter in the substring is a vowel,
3) for each 1 in pattern the corresponding letter is a consonant.

Your task is to calculate the number of substrings of source that match pattern.

Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'.
All other letters are consonants.
"""


def solution(pattern, source):
    vowels = "aeiouy"
    match_count = 0
    indices = [i for i, char in enumerate(pattern) if char == '0']
    pat_len = len(pattern)
    for i in range(len(source)):
        if i + pat_len > len(source):
            break
        source_slice = source[i: i + pat_len]
        truth_val = []
        if len(indices) != 0:
            for idx in indices:
                if source_slice[idx] in vowels:
                    truth_val.append(True)
                else:
                    truth_val.append(False)
        else:
            for i in range(len(vowels)):
                if vowels[i] in source:
                    return 0
        if False in truth_val:
            match_count += 0
        else:
            match_count += 1
    return match_count


def solution(pattern, source):
    vowels = "aeiouy"
    match_count = 0
    pat_len = len(pattern)
    for i in range(len(source) - pat_len + 1):
        substring = source[i:i+pat_len]
        if all((c in vowels and p == '0') or (c not in vowels and p == '1') for c, p in zip(substring, pattern)):
            match_count += 1
    return match_count
