def get_max():
    grades =[9.6, 9.2, 9.7]
    grades.sort(reverse=True)
    return grades[0]



# calculate the maximum value of the grades list
print(get_max())