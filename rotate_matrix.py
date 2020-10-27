# import numpy as np
#
a = [[1, 2], [3, 4]]
n = 3


def rotate(matrix):
    def rotate_pos_clockwise(i, j):
        return j, n - 1 - i

    n = len(matrix)
    if n <= 1:
        return
    for i in range((n + 1) // 2):
        for j in range(i, n - i - 1):
            up_val = matrix[i][j]
            i_right, j_right = rotate_pos_clockwise(i, j)
            i_bottom, j_bottom = rotate_pos_clockwise(i_right, j_right)
            i_left, j_left = rotate_pos_clockwise(i_bottom, j_bottom)
            matrix[i][j] = matrix[i_left][j_left]
            matrix[i_left][j_left] = matrix[i_bottom][j_bottom]
            matrix[i_bottom][j_bottom] = matrix[i_right][j_right]
            matrix[i_right][j_right] = up_val


rotate(a)
print(a)
