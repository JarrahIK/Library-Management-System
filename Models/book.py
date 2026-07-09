class Book:
    def __init__(self,title,author,year,isbn,is_available):
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
        self.available=is_available
    def __str__(self):
         return f"{self.title} {self.author} {self.year} {self.isbn}"
