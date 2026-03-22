from quality_enum import Quality
from status_enum import Status

class BookInstance:
    def __init__(self, id, quality = Quality.GOOD, status = Status.AVAILABLE, book = None):
        self.__id = id
        self.__quality = quality
        self.__status = status
        self.__book = book  # book object that this book instance belongs to
        self.__user = None
        
    def get_id(self):
        return self.__id
    
    def get_quality(self):
        return self.__quality
    
    def get_status(self):
        return self.__status
    
    # Updating status of instance
    def set_status(self, status):
        self.__status = status

    # Updating quality of instance
    def set_quality(self, quality):
        self.__quality = quality

    def get_user(self):
        return self.__user
    
    def set_user(self, user):
        self.__user = user

    def get_book(self):
        return self.__book
        