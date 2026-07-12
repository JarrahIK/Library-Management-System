import json
from Models.book import Book
class Library:
    def __init__(self):
        self.books=[]

    #Find the Book Using the Unique ISBN number
    def find_book_by_isbn(self,isbn):
        idx=0
        for b in self.books:
            if b.isbn==isbn:
             return idx
            idx+=1
        return None
    
    #Add books to the Library 
    def add_book(self,book):
        self.books.append(book)
    #Remove a book from the Library using its Unique ISBN
    def remove_book(self,isbn):
        V=self.find_book_by_isbn(isbn)
        if V is not None:
            self.books.pop(V)
            return True
        return False
    #Borrow a book from the Library Sets it unavialable for borrow until returned
    def borrow_book(self,isbn):
        V=self.find_book_by_isbn(isbn)
        if V is not None:
         return (self.books[V].borrow())
    #return book and it sets it available     
    def return_book(self,isbn):
        V=self.find_book_by_isbn(isbn)
        if V is not None:
            return(self.books[V].return_book())
    #search the book by title and return all books with the same title    
    def search_by_title(self,title):
        books_with_same_title=[]
        for b in self.books:
            if b.title==title:
                books_with_same_title.append(b.isbn)
        return books_with_same_title
    #search the book by author and return all books with the same author
    def search_by_author(self,author):
        books_with_author_name=[]
        for b in self.books:
            if b.author==author:
                books_with_author_name.append(b.title)
        return books_with_author_name
    #Print out all books currntly in the library
    def show_all_books(self):
        for b in self.books:
            print(b)
    #show borrowed books or unavailable books
    def show_borrowed_books(self):
        borrowed_books=[]
        for b in self.books:
            if not b.is_available:
                borrowed_books.append(b.isbn)
        print(borrowed_books)

    def save_books(self, filename):
        json_list=[]
        for b in self.books:
            json_list.append(b.to_dict())
        with open(filename, "w") as f:
            json.dump(json_list,f,indent=4)

    def load_books(self, filename):

      try:
         with open(filename, "r") as f:
            json_books = json.load(f)

         new_books = []

         for book in json_books:
            new_books.append(Book.from_dict(book))

         self.books = new_books

      except FileNotFoundError:
        print("File does not exist")

      except json.JSONDecodeError:
        print("The JSON file is corrupted")

      except KeyError:
         print("Missing Data!")

