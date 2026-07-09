class Book:
    def __init__(self,title,author,year,isbn):
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
    def __str__(self):
         return f"{self.title} {self.author} {self.year} {self.isbn}"
