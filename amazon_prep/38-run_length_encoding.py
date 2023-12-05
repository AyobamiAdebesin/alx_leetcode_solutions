#!/usr/bin/python3

def encoding(s):
    out = ''
    count = 1
    prev_char = s[0]
    for char in s[1:]:
        if prev_char == char:
            count += 1
        else:
            out += f"{str(count)}{prev_char}"
            prev_char = char
            count = 1
    out += f"{str(count)}{prev_char}"
    return out


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaa"
    print(encoding(s))

