def sum_of_rows(list_2D):

    row_sums = []

    for i in range(len(list_2D)):

        row_sum = 0

        #print(list_2D[i])

        for j in range(len(list_2D[i])):
            row_sum = row_sum + list_2D[i][j]

        row_sums.append(row_sum)

    return row_sums



print(sum_of_rows([[1,2,3],
                   [4,5,6],
                   [7,8,9]
                   ]))
print(sum_of_rows([[1],[2],[3]]))
print(sum_of_rows([[1,2,3],[4,5,6],[7,8,9]]))