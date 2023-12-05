#!/usr/bin/python3

def rotate_2d_a(a):
    """ Rotate a 2D a in place in a 90 degree clockwise direction """
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[j][i], a[i][j] = a[i][j], a[j][i]
    for i in range(len(a)):
        a[i] = a[i][::-1]

if __name__ == "__main__":
    a = [[1,2,3], [4,5,6], [7,8,9]]
    rotate_2d_a(a)
    print(a)