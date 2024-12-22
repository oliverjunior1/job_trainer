# # 1) without using with statement
# file = open('file_path', 'w')
# file.write('hello world!')
# file.close()
#
# # 2) without using with statement
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
#
# x = open('file_path', 'r')
#
# print(x.read())

# using with statement
with open('file_path', 'w') as file:
    file.write('Jesus is the way!')

x = open('file_path', 'r')

print(x.read())