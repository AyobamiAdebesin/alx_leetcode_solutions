#!/usr/bin/python3
""" Given a square of grid characters in the range [a-z],
rearrange elements of each row alphabetically, ascending.
Determine if the columns are also in ascending order, top to
bottom. Return YES if they are or NO if they are not """


def gridChallenge(grid):
    # Write your code here
    """ Check if each column is sorted """
    sorted_grid = sort_grid(grid)
    a = ["".join(col) for col in zip(*sorted_grid)]
    truth_val = []
    for elem in a:
        if "".join(sorted(elem)) == elem:
            truth_val.append("YES")
        else:
            truth_val.append("NO")
    if "NO" in truth_val:
        return "NO"
    else:
        return "YES"

def sort_grid(grid):
    """ Sort each row in the grid """
    for i in range(len(grid)):
        row = grid[i]
        grid[i] = "".join(sorted(row))
    return grid


if __name__ == "__main__":
    print(gridChallenge(["uxf", "vof", "hmp"]))