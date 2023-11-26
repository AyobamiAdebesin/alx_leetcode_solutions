#!/usr/bin/python3

def timeConversion(s):
    # Write your code here
    new_s = s.split(':')
    result = ""
    if new_s[-1].endswith("PM"):
        if int(new_s[0]) == 12:
            result+=new_s[0]
            result+=":"
            result+=new_s[1]
            result+=":"
            result+=new_s[2][0:2]
        else:
            result+= str(int(new_s[0]) + 12)
            result+=":"
            result+= new_s[1]
            result+=":"
            result+= new_s[2][:2]
    elif new_s[-1].endswith("AM"):
        if int(new_s[0]) == 12:
            result += "00:"
            result+=new_s[1]
            result+=":"
            result+=new_s[2][0:2]
        else:
            result+=new_s[0]
            result+=new_s[1]
            result+=new_s[2][0:2]
        
    return result

if __name__ == "__main__":
    s = "12:40:22AM"
    print(timeConversion(s))
