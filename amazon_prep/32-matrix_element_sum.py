#!/usr/bin/python3
"""
After becoming famous, the CodeBots decided to move
into a new building together. Each of the rooms has
a different cost, and some of them are free, but
there's a rumour that all the free rooms are haunted!
Since the CodeBots are quite superstitious, they refuse
to stay in any of the free rooms, or any of the rooms
below any of the free rooms.

Given matrix, a rectangular matrix of integers, where
each value represents the cost of the room, your task
is to return the total sum of all rooms that are suitable
for the CodeBots (ie: add up all the values that don't
appear below a 0).
"""


def solution(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i + 1 == len(matrix):
                    continue
                elif i + 1 != len(matrix):
                    k = i
                    while k < len(matrix):
                        matrix[k][j] = 0
                        k += 1
            else:
                sum += matrix[i][j]
    return sum


if __name__ == "__main__":
    matrix = [[4, 0, 1],
              [10, 7, 0],
              [0, 0, 0],
              [9, 1, 2]]
    print(solution(matrix))
