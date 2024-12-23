with open('story.txt', 'r') as y:
    x = y.read()
    y.close()

with open('story_copy.txt', 'w') as z:
    a = z.write(x)