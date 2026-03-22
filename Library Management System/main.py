from library import Library
from user import User
from book import Book
from book_instance import BookInstance
from quality_enum import Quality
from status_enum import Status

class ServiceLogic:
    def __init__(self):
        self.__library = Library()

    def create_user(self, name, id):
        user = User(name, id)
        try:
            self.__library.add_user(user)
        except Exception as e:
            print(str(e))

    def create_book(self, title, author, year, id):
        book = Book(title, author, year, id)
        try:
            self.__library.add_book(book)
        except Exception as e:
            print(str(e))

    def create_book_instance(self, id, book_id, quality = Quality.GOOD, status = Status.AVAILABLE):
        book = self.__library.get_book(book_id)
        if not book:
            print("Book does not exist")
            return
    
        book_instance = BookInstance(id, quality, status, book)
        try:
            self.__library.add_book_instance(book_instance)
        except Exception as e:
            print(str(e))

    def borrow_book(self, user_id, book_id, book_instance_id):
        user = self.__library.get_user(user_id)
        if not user:
            print("User does not exist")
            return
        
        try:
            self.__library.borrow_book(user, book_id, book_instance_id)
            print("Book instance is borrowed successfully")
        except Exception as e:
            print(str(e))

    def return_book(self, user_id, book_id, book_instance_id):
        user = self.__library.get_user(user_id)
        if not user:
            print("User does not exist")
            return
        
        try:
            self.__library.return_books(user, book_id, book_instance_id)
            print("Book instance is returned successfully")
        except Exception as e:
            print(str(e))

    def user_borrowed_books(self, user_id):
        user_records = self.__library.user_borrowed_books(user_id)
        if not user_records:
            print("User does not have any borrowed books")
            return
        
        for book_instance_id in user_records:
            book_instance = user_records[book_instance_id]
            print(f"Book Instance ID: {book_instance.get_id()}")
            print(f"Book Instance Quality: {book_instance.get_quality()}")
            print(f"Book Instance Status: {book_instance.get_status()}")
            print(f"Book Instance User: {book_instance.get_user().get_name()}")
            print(f"Book Instance Book: {book_instance.get_book().get_title()}")

if __name__ == "__main__":
    service = ServiceLogic()
    print("Welcome to Library Management System")

    # Hardcoded values for testing
    service.create_user("Stanly", 1)
    service.create_user("John", 2)
    service.create_user("Tom", 3)

    service.create_book("Python", "John Doe", 2022, 1)
    service.create_book("Java", "John Doe", 2022, 2)
    service.create_book("C++", "John Doe", 2022, 3)

    # 3 Book Instances for each book
    service.create_book_instance(1, 1)
    service.create_book_instance(2, 1)
    service.create_book_instance(3, 1)

    service.create_book_instance(4, 2)
    service.create_book_instance(5, 2)
    service.create_book_instance(6, 2)

    service.create_book_instance(7, 3)
    service.create_book_instance(8, 3)
    service.create_book_instance(9, 3)

    while True:
        user_id = int(input("Enter user id: "))
        book_id = int(input("Enter book id: "))
        book_instance_id = int(input("Enter book instance id: "))

        operation_type = int(input("Enter operation type 1: Borrow Book, 2: Return Book 3: View Borrowed Books: "))
        if operation_type == 1:
            service.borrow_book(user_id, book_id, book_instance_id)
        elif operation_type == 2:
            service.return_book(user_id, book_id, book_instance_id)
        elif operation_type == 3:
            service.user_borrowed_books(user_id)
        else:
            break

