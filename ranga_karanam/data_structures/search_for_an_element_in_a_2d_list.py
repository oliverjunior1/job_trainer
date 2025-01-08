def search_element(list_2d, target):
    for i in range(len(list_2d)):
        for j in range(len(list_2d[i])):
            if list_2d[i][j] == target:
                return (i, j)

    return (-1,-1)


print(search_element([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],5))