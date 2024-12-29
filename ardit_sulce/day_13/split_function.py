def get_nr_items(user_input):
    x = user_input.split(',')
    return len(x)

print(get_nr_items('john,lisa,teresa'))