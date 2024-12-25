def get_max():
    grades =[9.6, 9.2, 9.7]
    grades.sort(reverse=True)
    #change the function to return:
    return f"Max: {grades[0]}, Min: {grades[-1]}"

# show the result
print(get_max())
