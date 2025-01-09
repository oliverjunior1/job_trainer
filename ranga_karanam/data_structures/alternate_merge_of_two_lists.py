def alternate_merge(list1, list2):

    merged_list = []

    max_length = max(len(list1), len(list2))

    for i in range(max_length):

        if i < len(list1):
            merged_list.append(list1[i])

        if i < len(list2):
            merged_list.append(list2[i])

    return merged_list



print(alternate_merge(['a', 'b'],['c','d','e']))