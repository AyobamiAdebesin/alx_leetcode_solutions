# #!/usr/bin/python3
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# #
# # Complete the 'getScoreDifference' function below.
# #
# # The function is expected to return a LONG_INTEGER.
# # The function accepts INTEGER_ARRAY points as parameter.
# #

# def getScoreDifference(points):
#     # Write your code here
#     score_a = 0
#     score_b = 0
#     count = 0
#     while len(points) != 0:
#         if count % 2 == 0:
#             max_score = max(points)
#             score_a+=max_score
#             points.remove(max_score)
#             count += 1
#         elif count %2 != 0:
#             max_score = max(points)
#             score_b += max_score
#             points.remove(score_b)
#             count += 1
#     return abs(score_a - score_b)
        

# if __name__ == '__main__':



#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'matchStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY text
#  2. STRING_ARRAY pat
#

def matchStrings(text, pat):
    # Write your code here
    output = [''] * len(text)
    for i in range(len(text)):
        strng = text[i]
        the_pat = pat[i]
        idx = the_pat.index('*')
        part1 = the_pat[0:idx]
        part2 = the_pat[idx+1:]
        len_part1 = len(part1)
        part1_text = strng[0:len_part1]
        part2_text = strng[len(strng) - len_part2:]
        # pat_len = len(the_pat)
        if part1_text == part1 and part2_text == part2:
            output[i] += 'YES'
        elif part1 == '' and part2_text == part2:
            output[i] += 'YES'
        elif part2 == '' and part1_text == part1:
            output[i] += 'YES'
        # if part1 in string
        # elif part1 in strng and part2 not in strng:
        #     output[i] += 'NO'
        # elif part1 not in strng and part2 in strng:
        #     output[i] += 'NO'
        else:
            output[i] += 'NO'
    return output
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     text_count = int(input().strip())

#     text = []

#     for _ in range(text_count):
#         text_item = input()
#         text.append(text_item)

#     pat_count = int(input().strip())

#     pat = []

#     for _ in range(pat_count):
#         pat_item = input()
#         pat.append(pat_item)

#     result = matchStrings(text, pat)

#     fptr.write('\n'.join(result))
#     fptr.write('\n')

#     fptr.close()



# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'getScoreDifference' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY points as parameter.
#

# def getScoreDifference(points):
#     # Write your code here
#     score_a = 0
#     score_b = 0
#     count = 2
#     while len(points) != 0:
#         if count % 2 == 0:
#             max_score = max(points)
#             score_a+=max_score
#             points.remove(max_score)
#             count += 1
#         elif count % 2 == 1:
#             max_score = max(points)
#             score_b += max_score
#             points.remove(max_score)
#             count += 1
#     return abs(score_a - score_b)

