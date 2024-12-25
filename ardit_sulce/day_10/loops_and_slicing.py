filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

x = [y for y in filenames]
for a in x:
    print(a[:-4].capitalize())
