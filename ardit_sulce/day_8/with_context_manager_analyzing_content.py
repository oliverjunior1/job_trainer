file = open("essay.txt", 'r')
content = file.read()
file.close()

nr_chars = len(content)
print(nr_chars)