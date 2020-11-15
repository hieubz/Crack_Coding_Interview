def zero_matrix(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])

    row = [0] * num_row
    col = [0] * num_col

    for i in range(num_row):
        for j in range(num_col):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for r in row:
        if r == 1:
            zero_row(matrix, r)

    for c in col:
        if c == 1:
            zero_col(matrix, c)


def zero_matrix_no_space(matrix):
    first_row_null = False
    first_col_null = False

    # check first row and col which has any 0 element => nullify at the end
    for i in matrix[0]:
        if i == 0:
            first_row_null = True
            break

    for i in matrix[:][0]:
        if i == 0:
            first_col_null = True
            break

    # for from 1 to end
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # nullify cols
    for i in range(1, len(matrix[0])):
        # iterate through first row
        if matrix[0][i] == 0:
            zero_col(matrix, i)

    # nullify rows
    for i in range(1, len(matrix)):
        # iterate through first col
        if matrix[i][0] == 0:
            zero_row(matrix, i)

    # nullify itself
    if first_col_null:
        zero_col(matrix, 0)

    if first_row_null:
        zero_row(matrix, 0)


def zero_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def zero_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
