def greeti(message):
    new_message = message.capitalize()
    print('Hey hey')
    return new_message

greet_typed = input("Type your greeting:")
greeting = greeti(greet_typed)

print(greeting)


