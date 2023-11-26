"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock."""

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
            result+=":"
            result+=new_s[1]
            result+=":"
            result+=new_s[2][0:2]
        
    return result