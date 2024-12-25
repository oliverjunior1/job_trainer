passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

#loop over the passwords list
x = [y for y in passwords if len(y) < 8]

#show all less than 8
for a in x:
    print(a)