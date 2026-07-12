from Services.library import Library
from Models.book import Book

# Create first library
library = Library()

book1 = Book("Clean Code", "Robert Martin", 2008, "111")
book2 = Book("Python", "Guido", 2020, "222")

library.add_book(book1)
library.add_book(book2)

print(library.find_book_by_isbn("222"))