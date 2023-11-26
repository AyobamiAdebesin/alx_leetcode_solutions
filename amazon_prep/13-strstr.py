#!/usr/bin/python3


def strstr(haystack, needle):
    """
    Finds the first occurrence of the substring 'needle' in the string 'haystack'.

    :param haystack: The input string.
    :param needle: The substring to search for.
    :return: The index of the first occurrence of 'needle' in 'haystack', or -1 if not found.
    """
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


if __name__ == "__main__":

    # Example usage:
    haystack = "Hello, World! This is a sample string."
    needle = "World"
    result = strstr(haystack, needle)

    if result != -1:
        print(f"Substring '{needle}' found at index {result}.")
    else:
        print(f"Substring '{needle}' not found in the given string.")
