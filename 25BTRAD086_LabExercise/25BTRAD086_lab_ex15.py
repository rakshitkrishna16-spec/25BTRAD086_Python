class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' has been returned.")

b1 = Book("Python Programming")
b1.issue_book()
b1.issue_book()
b1.return_book()