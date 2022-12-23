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
        print()
        for book in self.list:
            book.print()
        print()

    def removeBook(self, name):
        for i in range(len(self.list)):
            if self.list[i].title == name:
                self.list.pop(i)
                print("Book removed!")
                return


def main():
    print("Welcome to your library!")
    libName = input("Please enter the name of your library: ")
    lib = Library(libName)
    while True:
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Print all books")
        print("4. Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            pages = input("Enter the number of pages in the book: ")
            book = Book(title, author, pages)
            lib.addBook(book)
        elif choice == "2":
            name = input("Enter the name of the book you want to remove: ")
            lib.removeBook(name)
        elif choice == "3":
            lib.printBooks()
        elif choice == "4":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice, please try again!")

main()
