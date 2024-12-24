contents = ['All carrots are to be sliced longitudinally.',
            'The carrots were reportedly sliced.',
            'The slicing process was well presentated']

filenames = ['doc.txt', 'report.txt', 'presentations.txt']

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)

a = 'I am a string on my own'

