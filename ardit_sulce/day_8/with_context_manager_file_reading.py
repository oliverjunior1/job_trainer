# Using a context manager to read the file
with open("bear.txt", "r") as file:
    content = file.read()

print(content)
