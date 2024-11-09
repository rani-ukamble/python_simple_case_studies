# Create a Simple Class:

# Create a class Person with attributes name, age, and city.
# Write an __init__ method to initialize these attributes.
# Write a method introduce that prints a self-introduction.
# Example: My name is John, I am 25 years old, and I live in New York.


# class person:
#     def __init__(self):
#         self.name = "rk"
#     def intro(self):
#         print(f"My name is {self.name}")

# obj = person()
# obj.intro()



# Task 1: Library and Book System

# Create two classes: Book and Library.

# Book should have attributes like title, author, and year.
# Library should store a list of books.
# Implement a method __str__() in Book that returns the book details.
# Write a method in Library to add books, remove books, and list all books.

class Book:
    def __init__(self,title, author, year):
        self.title =title
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"     

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
    
    def remove_books(self, book):
        for book in self.books:
            self.books.remove(book)
            
    def show_books(self):
        for book in self.books:
            print(book)

b1 = Book("Math1", "vikas", "2024")
b2 = Book("Math2", "vikas", "2024")
b3 = Book("Math3", "vikas", "2024")

l = Library()
l.add_books(b1)
l.add_books(b2)
l.add_books(b3)

l.show_books()


