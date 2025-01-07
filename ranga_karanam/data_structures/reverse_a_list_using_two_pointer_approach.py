def reverse_list(list):
    start = 0
    end = len(list) - 1

    while(start < end):
        print(list)
        print(f'end iteration - {start} {end}')
        list[start], list[end] = list[end], list[start]
        print(list)
        start += 1
        end -= 1
        print(f'end iteration - {start} {end}')


    return list

# Testing the function with examples
print(reverse_list([10,20,30]))
print(reverse_list([5,15,25,35]))
print(reverse_list([1]))

