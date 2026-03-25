class Group:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__members = {}
        self.balances = {}
        self.__expenses = {}
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_members(self):
        return self.__members
    
    def add_member(self, member):
        id = member.get_id()

        if id not in self.__members:
            self.__members[id] = member
        else:
            raise Exception("Member already exists")
        
        print(f'Members are {self.__members}')
        
    def remove_member(self, member):
        id = member.get_id()

        if id in self.__members:
            del self.__members[id]
        else:
            raise Exception("Member does not exist")
        print(f'Members are {self.__members}')
        
    def add_expense(self, expense):
        id = expense.get_id()

        if id not in self.__expenses:
            self.__expenses[id] = expense
        else:
            raise Exception("Expense already exists")

        