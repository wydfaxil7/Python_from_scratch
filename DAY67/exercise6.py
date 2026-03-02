########## Library management system ##########
class Library:

    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def showInfo(self):
        print(f"Total number of books in Library is {self.no_of_books}. The books are:")
        for book in self.books:
            print(book)
            
l1 = Library()
l1.add_book("Python")
l1.add_book("Python and Kotlin")
l1.add_book("Python and Java")
l1.add_book("Python and C++")
l1.showInfo()