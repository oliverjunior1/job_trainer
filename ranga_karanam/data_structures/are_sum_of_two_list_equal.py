def are_sums_equal(list1, list2):
    if not list1 or not list2:
        return False
    sum1 = 0
    sum2 = 0
    sum1 = sum(list1)
    sum2 = sum(list2)
    for x in list1:
        sum1 += x
    for y in list2:
        sum2 += y

    if sum1 == sum2:
        return True
    else:
        return False

print(are_sums_equal([10, 20, 30], [15, 25, 20]))  # Output: True
print(are_sums_equal([5, 10, 15], [5, 10, 14]))  # Output: False
print(are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1]))  # Output: True
print(are_sums_equal([], [4, 3, -7]))  # Output: False
print(are_sums_equal([1, 2], []))  # Output: False

