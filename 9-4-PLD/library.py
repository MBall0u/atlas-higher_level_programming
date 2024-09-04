#!/usr/bin/python3
class book:
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

HP1 = ("Happy Potter 1", "JK Rowling", False)
HP2 = ("Happy Potter 2", "JK Rowling", False)
HP3 = ("Happy Potter 3", "JK Rowling", False)
HP4 = ("Happy Potter 4", "JK Rowling", False)

class library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book_by_title(self, title):
        for i in self.books:
            if i.title == title:
                return i.title, i.author, i.is_checked_out
    
    def list_available_books(self):
        available_list = []
        for i in self.books:
            if i.is_checked_out == False:
                available_list.append(i)
        return available_list

class member:
    def __init__(self, name, borrowed_books=[]):
        self.name = name
        self.borrowed_books = borrowed_books
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.is_checked_out = True

    def return_book(self, book):
        for i in self.borrowed_books:
            if i.title == book.title:
                self.borrowed_books.remove(book)
                i.is_checked_out = False

M1 = member("LeBron James")
M2 = member("Tiger Woods")
M3 = member("Stephen A. Smith")

new_library = library()
new_library.add_book(HP1)
new_library.add_book(HP2)
new_library.add_book(HP3)
new_library.add_book(HP4)

for book in new_library.list_available_books():
    print("Title: {}, Author: {}, Checked out: {}".format(book.title, book.author, book.is_checked_out))

M1.borrow_book(HP1)
M2.borrow_book(HP3)

for book in new_library.list_available_books():
    print("Title: {}, Author: {}, Checked out: {}".format(book.title, book.author, book.is_checked_out))
    