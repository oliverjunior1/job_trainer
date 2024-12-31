class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def __str__(self):
        return f"The country is {self.name} and its capital is {self.capital}."

brazil = Country("Brazil", 'Brasilia')
india = Country('India', 'New Delhi')
usa = Country('USA', 'Washington')

print(brazil)
print(india)
print(usa)