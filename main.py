from Services.library import Library
from Models.book import Book

city_library=Library()
book1=Book(
    input("Enter Book title "),
    input("Enter Book author "),
    int(input("Enter Book year ")),
    input("Enter Book isbn "),
    True
)



city_library.add_book(book1)

if city_library.remove_book(book1.isbn):
    print("Book removed successfully.")
else:
    print("Book not found.")

