try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    #calculate the percentage
    percentage = value/total_value*100
    print(f'That is {percentage}%')
except :
    print('You need to enter a number. Run the program again.')