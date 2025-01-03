class Book:
    def __init__(self, name, copies=0):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much

the_art_of_computer_programming = Book('The Art of Computer Programming')
the_art_of_computer_programming.increase_copies(10)
the_art_of_computer_programming.decrease_copies(3)
the_art_of_computer_programming.increase_copies(15)

the_origin_of_inequality = Book('The Origin Of Inequality')
the_origin_of_inequality.increase_copies(30)

print(the_art_of_computer_programming.name, the_art_of_computer_programming.copies)
print(the_origin_of_inequality.name, the_origin_of_inequality.copies)