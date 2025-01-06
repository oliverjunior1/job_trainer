# Define a function with two parameters
def has_greater_element(numbers, value):
    # if the numbers list is empty, return False
    if not numbers:
        return False
        # Iterate through the numbers using a for loop
    for x in numbers:
        # in all the iteration, use a if statement to check if the current number is greater than value
        if x > value:
            # If a greater number is found after checking all the numbers, return True from the function
            return True

        # Else return False
    return False

print(has_greater_element([10,20,30],15))
print(has_greater_element([5,7,8],10))
print(has_greater_element([],5))
