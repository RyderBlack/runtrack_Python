class Book:
    def __init__(self, author, nb_pages):
        self.__author = author
        self.__nb_pages = nb_pages
        
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

    def __str__(self):
        return f"The author's name is {self.__author} and the number of pages in this book is {self.__nb_pages}"
    
    
book_01 = Book("Harry Potter", 322)

print(book_01)
book_01.set_nb_pages(-44)

print(book_01)
    