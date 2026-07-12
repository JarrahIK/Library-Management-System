class Book:
    def __init__(self,title,author,year,isbn,is_available=True):
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
        self.is_available=is_available
    def __str__(self):
         return f"{self.title} {self.author} {self.year} {self.isbn}"
    def borrow(self):
        if self.is_available:
            self.is_available=False
            return True
        else:
            return False
    def return_book(self):
        if not self.is_available:
            self.is_available=True
            return True
        else:
            return False
    def to_dict(self):
        return {
            "title":self.title,
            "year":self.year,
            "author":self.author,
            "isbn":self.isbn,
            "is_available":self.is_available
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
        data["title"],
        data["author"],
        data["year"],
        data["isbn"],
        data["is_available"]
        )    