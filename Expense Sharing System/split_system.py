from user import User
from group import Group
from expense import Expense

class SplitSystem:
    def __init__(self):
        self.__users = {}
        self.__groups = {}
    
    def add_user(self, id, name, email):
        if id in self.__users:
            raise Exception("User already exists")
        
        self.__users[id] = User(id, name, email)
        print(f'Users are {self.__users}')

    def make_group(self, id, name, member_ids):
        if id in self.__groups:
            raise Exception("Group already exists")
        
        if len(member_ids) < 2:
            raise Exception("Group must have at least 2 members")
        
        self.__groups[id] = Group(id, name)

        for member_id in member_ids:
            self.__groups[id].add_member(self.__users[member_id])

        print(f'Groups are {self.__groups}')

    def remove_member_from_group(self, group_id, member_id):
        self.__groups[group_id].remove_member(self.__users[member_id])

    def get_group_members(self, group_id):
        return self.__groups[group_id].get_members()

    def add_expense(self, id, amount, description, expense_creator_id, group_id, type = 'GENERAL', user_percentages = {}):
        group = self.__groups[group_id]

        expense_creator = self.__users[expense_creator_id]
        expense = Expense(id, amount, description, expense_creator, group)

        group.add_expense(expense)

        members = group.get_members()
        size = len(members)

        if type == 'GENERAL':
            for member in members:
                if member == expense_creator_id:
                    continue

                individual_amount = amount/size
                self.add_user_expense(expense_creator_id, individual_amount, member, group)

        else:
            for percentage in user_percentages:
                if percentage == expense_creator_id:
                    continue
                split_amount = amount * user_percentages[percentage] / 100
                self.add_user_expense(expense_creator_id, split_amount, percentage, group)

        print(f'group balances are {group.balances}')

    def add_user_expense(self, expense_creator_id, amount, member_id = None, group = None):
        if member_id not in group.balances:
            group.balances[member_id] = {}

        if expense_creator_id not in group.balances:
            group.balances[expense_creator_id] = {}

        user_owes_member = group.balances.get(expense_creator_id, {}).get(member_id, 0)
        diff = amount - user_owes_member

        if diff > 0:
            group.balances[member_id][expense_creator_id] = diff
            group.balances[expense_creator_id][member_id] = 0

        else:
            group.balances[member_id][expense_creator_id] = 0
            group.balances[expense_creator_id][member_id] = -diff if diff<0 else 0

