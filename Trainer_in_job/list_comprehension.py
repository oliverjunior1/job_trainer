# fruits = ["apple", "melon", "water melon", "cherry", "grape"]
# newfruits = []
#
# for x in fruits:
#     if "a" in x:
#         newfruits.append(x)
#
# print(newfruits)

# We will make the same thing with less type

fruits = ["apple", "melon", "water melon", "cherry", "grape"]

newfruits = [x for x in fruits if 'a' in x]

print(newfruits)