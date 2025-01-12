class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr( (self.id, self.name, self.author, self.reviews) )

    def add_review(self, review):
        self.reviews.append(review)

book = Book(123,'Devops', 'Rango')


class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))

review = Review(10, 'Great Book', 5)
print(review)
book.add_review(review)
print(book)