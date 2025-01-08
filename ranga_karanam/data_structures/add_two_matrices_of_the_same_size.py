def add_matrices(matrix1, matrix2):

    result = []

    for i in range(len(matrix1)):

        row_result = []

        for j in range(len(matrix1[i])):
            sum = matrix1[i][j] + matrix2[i][j]
            row_result.append(sum)

        result.append(row_result)

    return result



# Testing the function
print(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # Output: [[6, 8], [10, 12]]
print(add_matrices([], []))  # Output: []
