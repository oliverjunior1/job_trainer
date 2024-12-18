countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

# Pair each country with its corresponding filename
for country, filename in zip(countries, filenames):
    # Open the file in write mode and write the country name
    with open(filename, 'w') as file:
        file.write(country)

print("Countries have been written to their respective files.")


