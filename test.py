from ctypes import *

import library

print(library.version())

class CBook(Structure):
    _fields_= [("book_name", c_wchar_p),
              ("book_type", c_wchar_p),
              ("book_author", c_wchar_p),
              ("num_of_pages", c_int)]

class CLibrary(Structure):
    _fields_= [("book_list", CBook * 100),
               ("books_stored", c_int)]

    # def __init__(self, book_list, books_stored=0):
    #     super(CLibrary, self).__init__(books_stored)

    def books_stored_to_zero(self):

        self.books_stored = 0



new_book = CBook("Harry Potter", "Children", "JK Rowling", 345)

print (new_book.book_name)

lib = CLibrary()

lib.books_stored_to_zero()

print(lib)

print("Books stored in lib = %d" % lib.books_stored)



result = c_int()
result = library.addBook(lib, "Harry Aotter", "Ahildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Botter", "Bhildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Cotter", "Children", "JK Rowling", 345)
result = library.addBook(lib, "Harry Dotter", "Dhildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Eotter", "Ehildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Fotter", "Fhildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Gotter", "Ghildren", "JK Rowling", 345)
result = library.addBook(lib, "Harry Hotter", "Hhildren", "JK Rowling", 345)

print("I am here")
result = library.addBook(lib, "Lost", "Adult", "Damian ", 111)

print(result)
print("Done")