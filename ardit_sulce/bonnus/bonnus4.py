filenames = ['1.Raw Data.txt', '2.Reposts.txt', '3.Presentations.txt']

for filename in filenames:
    filename = filename.replace('.', '-',1)
    print(filename)