class Expense:
    def __init__(self, id, amount, description, user, group):
        self.__id = id
        self.__amount = amount
        self.__description = description
        self.__user = user
        self.__group = group

    def get_id(self):
        return self.__id
    
    def get_amount(self):
        return self.__amount
    
    def get_description(self):
        return self.__description
    
    def get_user(self):
        return self.__user





