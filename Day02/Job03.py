class Book:
    def __init__(self, author, nb_pages):
        self.__author = author
        self.__nb_pages = nb_pages
        self.__available = True
        
    def get_author(self):
        return self.__author
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_author(self, new_author_name):
        self.__author = new_author_name
        return self.__author
    
    def set_nb_pages(self, new_nb_pages):
        if new_nb_pages >= 0 and new_nb_pages.is_integer():
            self.__nb_pages = new_nb_pages
            return self.__nb_pages
        else:
            raise ValueError("the number should be a positive integer")
        
    def verification(self):
        if self.__available:
            return True
        else:
            return False
        
    def rent_book(self):
        if self.verification():
            self.__available = False
            return True
        else:
            return False
        
    def return_book(self):
        if not self.verification():
            self.__available = True
            return True
        else:
            return False

    def __str__(self):
        return f"The author's name is {self.__author} and the number of pages in this book is {self.__nb_pages}"
    
    
book_01 = Book("Harry Potter", 322)

# print(book_01)
print(book_01.verification())
print(book_01.rent_book())
print(book_01.verification())
print(book_01.return_book())
print(book_01.verification())