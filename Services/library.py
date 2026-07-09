class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        book.is_available=True
    def remove_book(self,isbn):
        idx=0
        for b in self.books:
            if b.isbn==isbn:
                self.books.pop(idx)
                self.books[idx].is_available=False
                return True
            idx+=1
        return False
    def borrow_book(self):
        pass
    def return_book(self):
        pass
    def search_by_title(self,title):
        books_with_same_title=[]
        for b in self.books:
            if b.title==title:
                books_with_same_title.append(b.isbn)
        return books_with_same_title
    def search_by_author(self,author):
        books_with_author_name=[]
        for b in self.books:
            if b.author==author:
                books_with_author_name.append(b.title)
        return books_with_author_name
    def show_all_books(self):
        for b in self.books:
            print(b)
    def show_borrowed_books(self):
        pass
