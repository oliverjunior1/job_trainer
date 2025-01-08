def next_character(char):
    next_ascii_val = ord(char) + 1
    next_char = chr(next_ascii_val)
    return next_char

char = 'Y'
next_char = next_character(char)
print(f'Given character: {char}')
print(f'The next character is: {next_char}')