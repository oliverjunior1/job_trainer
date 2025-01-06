numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# for number in reversed(numbers):
#     print(number)

for number in sorted(numbers, key=len, reverse=True):
    print(number)


print(numbers)