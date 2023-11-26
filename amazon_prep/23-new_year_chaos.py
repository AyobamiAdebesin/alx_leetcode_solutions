#!/usr/bin/python3
""" 
Minimum bribe

It's new year day and people are in line for the
wonderland rollercoaster ride. Each person wears a sticker
indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them
to swap postions, but they stil wear their original sticker.
One person can bribe at most 2 others.

Determine the minimum number of bribes that took place to get
to a given queue order. Print the number of bribes, or if anyone
has bribes more than 2 people, print "Too Chaotic
"""


def minimum_bribe(q):
    # Write your code here
    no_of_shifts = [q[i] - 1 - i for i in range(len(q))]
    prev_is_2 = 0
    bribes = 0
    for shift in no_of_shifts:
        if shift > 2:
            print("Too chaotic")
            return
        elif shift == 2:
            prev_is_2 += 1
            bribes += shift
        else:
            # If the no_shift is < 2; we have 2 options:
            # no_shift == 1; means you bribed someone and you moved to the front of the queue(left)
            # no_shift == 0; you were not bribed, you are in your original position
            # no_shift < 0: means you were bribed and you moved to the back of the queue(right)
            new_value = max(shift + prev_is_2, 0)
            bribes += new_value
            prev_is_2 = 0

    print(bribes)

# def minimumBribes(q):
#     # Write your code here
#     no_bribes = 0
#     for i in range(0, len(q)):
#         if q[i] != i + 1:
#             no_shifts = q[i] - (i+1)
#             no_bribes+=no_shifts
#             if no_shifts > 2:
#                 return "Too chaotic"
#             elif
