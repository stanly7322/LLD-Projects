# Only have details of the book like title, author, year, id
class Book:
    def __init__(self, title, author, year, id):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id
        
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def get_id(self):
        return self.__id
    
    # For Updation of Book Meta Details
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_year(self, year):
        self.__year = year
