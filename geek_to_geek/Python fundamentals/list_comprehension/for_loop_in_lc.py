# a = [1,2,3,4,5]
#
# # Create an empty list 'res' to store results
# res = []
#
# # Iterate over each element in list 'a'
# for val in a:
#
#     # Multiply each element by 2 and append it to 'res'
#     res.append(val*2)
#
# print(res)
#--------------------------using_list_comprehension-----------------------
a = [1,2,3,4,5]

res = [val * 2 for val in a]

print(res)

