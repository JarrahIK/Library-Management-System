from Services.library import Library
from Models.book import Book

city_library=Library()
book1=Book("ibraheem","jj",1234,241414)
book2=Book("mohammad","mm",1234,198274)
book3=Book("jarrah","ii",4321,239242)
city_library.add_book(book1)
city_library.add_book(book2)
city_library.add_book(book3)
city_library.save_books("MyBooks")
city_library.load_books("MyBooks")
city_library.show_all_books()


