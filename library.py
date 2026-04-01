class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print(self.book_name, "checked out")
        else:
            print(self.book_name, "not available")

    def return_book(self):
        self.available = True
        print(self.book_name, "returned")

    def display(self):
        if self.available:
            print(self.book_name, "by", self.author, "- Available")


book1 = Library("Python Basics", "ABC")
book2 = Library("Data Science", "XYZ")

book1.checkout()
book1.display()
book1.return_book()
