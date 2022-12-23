# All classes and functions are defined here for readability

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def print(self):
        print(f"{self.title} by {self.author} with ({self.pages} pages)")

class Library:
    def __init__(self, name = "Library"):
        self.list = []
        self.name = name

    def addBook(self, book):
        self.list.append(book)
            
    def printBooks(self):
        for book in self.list:
            book.print()
    
b1 = Book("Harry Potter", "JK Rowling", 500)
b2 = Book("Lord of the Rings", "Tolkien", 700)
b3 = Book("The Hobbit", "Tolkien", 300)

lib = Library("My Library")

lib.addBook(b1)
lib.addBook(b2)
lib.addBook(b3)

