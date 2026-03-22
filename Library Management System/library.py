from status_enum import Status

class Library:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.book_instances = {}
        self.user_borrow_records = {}

    def add_user(self, user):
        user_id = user.get_id()
        if user_id not in self.users:
            self.users[user_id] = user
            print(f"Current users are : {self.users}")
        else:
            raise Exception("User already exists")
        
    def get_user(self, id):
        return self.users.get(id, None)
    
    def add_book(self, book):
        book_id = book.get_id()
        if book_id not in self.books:
            self.books[book_id] = book
            print(f"Current books are : {self.books}")
        else:
            raise Exception("Book already exists")
        
    def get_book(self, id):
        return self.books.get(id, None)

    def add_book_instance(self, book_instance):
        book = book_instance.get_book()
        book_id = book.get_id()
        book_instance_id = book_instance.get_id()

        if book_id not in self.books:
            raise Exception("Book does not exist")
        
        if book_id not in self.book_instances:
            self.book_instances[book_id] = {}
            self.book_instances[book_id][book_instance_id] = book_instance
            print(f"Current book instances are : {self.book_instances}")
            return

        book_instances = self.book_instances[book_id]
        if book_instance_id in book_instances:
            raise Exception("Book instance already exists")
        
        print(f"Current book instances are : {self.book_instances}")
        self.book_instances[book_id][book_instance_id] = book_instance

    def get_all_book_instances(self, book_id):
        return self.book_instances.get(book_id, {})
    
    def borrow_book(self, user, book_id, book_instance_id):
        if book_id not in self.books:
            raise Exception("Book does not exist")
        
        book_instance = self.book_instances.get(book_id, {}).get(book_instance_id)
        if not book_instance:
            raise Exception("Book instance does not exist")
        
        if book_instance.get_status() == Status.AVAILABLE:
            book_instance.set_status(Status.BORROWED)
            book_instance.set_user(user)

            if user.get_id() not in self.user_borrow_records:
                self.user_borrow_records[user.get_id()] = {}
            
            self.user_borrow_records[user.get_id()][book_instance.get_id()] = book_instance
            self.book_instances[book_id][book_instance_id] = book_instance
            return
        else:
            raise Exception("Book instance is not available")\
        
    def return_books(self, user, book_id, book_instance_id):
        if book_id not in self.books:
            raise Exception("Book does not exist")
        
        book_instance = self.book_instances.get(book_id, {}).get(book_instance_id)
        if not book_instance:
            raise Exception("Book instance does not exist")
        
        if book_instance.get_status() == Status.BORROWED:
            if book_instance.get_user().get_id() == user.get_id():
                book_instance.set_status(Status.AVAILABLE)                
                book_instance.set_user(None)

                del self.user_borrow_records[user.get_id()][book_instance.get_id()]
                self.book_instances[book_id][book_instance_id] = book_instance
                return
            else:
                raise Exception("Book instance is not borrowed by user")
            
        else:
            raise Exception("Book instance is not borrowed by user")
        

    def user_borrowed_books(self, user_id):
        if user_id not in self.user_borrow_records:
            return {}
        
        return self.user_borrow_records[user_id]

                
    


        


