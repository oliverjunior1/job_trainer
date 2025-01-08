def find_multiples(number, limit):
    multiples = []

    multiple = number

    while(multiple<limit):
        multiples.append(multiple)
        multiple += number

    return multiples

print(find_multiples(3,10))