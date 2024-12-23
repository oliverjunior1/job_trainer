languages = ['English', 'German', 'Spanish']

for x in languages:
    for a in languages:
        with open(f'{a}.txt', 'w') as y:
            y.write(f'{a}')