# Create a list
def is_list_sorted(list):
    # check for empty list
    if not list:
        return True
    # iterate and compare
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False

print(is_list_sorted([10, 20, 30]))   # Output: True
print(is_list_sorted([10, 30, 20]))   # Output: False
print(is_list_sorted([30, 20, 10]))   # Output: False
print(is_list_sorted([]))             # Output: True
