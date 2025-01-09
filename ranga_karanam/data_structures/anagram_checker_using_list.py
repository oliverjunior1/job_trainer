def is_anagram(string1, string2):

    if len(string1) != len(string2):
        return False

    list1 = [0] * 26

    list2 = [0] * 26

    for char in string1:
        list1[ord(char) - ord ('a')] += 1

    for char in string2:
        list2[ord(char) - ord ('a')] += 1

    return (list1 == list2)

#print(is_anagram('listen', 'silent'))

print(ord('s') - ord('a'))