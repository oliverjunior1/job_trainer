'''list1 = [0,0,0,0]
list2 = [0,0,0,0]
list3 = [0,0,0,0]

two_d_list_1 = [list1, list2, list3]

two_d_list_2 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
print(two_d_list_1)
print(two_d_list_2)'''

rows = 3
cols = 4

two_d_list = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i*10 *j)
    two_d_list.append(row)
    print(two_d_list)

two_d_list[2][3] = two_d_list[2][3] * 2

two_d_list[1][2] = two_d_list[1][2] * 2

print(two_d_list)

for i in range(rows):
    for j in range(cols):
        print(two_d_list[i][j], end=' ')
    print()

