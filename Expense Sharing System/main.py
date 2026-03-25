from split_system import SplitSystem

class ServiceLogic:
    def __init__(self):
        self.__split_system = SplitSystem()

    def add_user(self, id, name, email):
        try:
            self.__split_system.add_user(id, name, email)
        except Exception as e:
            print(str(e))

    def make_group(self, id, name, member_ids):
        try:
            self.__split_system.make_group(id, name, member_ids)
        except Exception as e:
            print(str(e))

    def get_group_members(self, group_id):
        return self.__split_system.get_group_members(group_id)
    
    def remove_member_from_group(self, group_id, member_id):
        self.__split_system.remove_member_from_group(group_id, member_id)
    
    def add_expense(self, id, amount, description, expense_creator_id, group_id, type = 'GENERAL', user_percentages = {}):
        self.__split_system.add_expense(id, amount, description, expense_creator_id, group_id, type, user_percentages)


if __name__ == "__main__":
    service_logic = ServiceLogic()

    # Testing users
    service_logic.add_user(1, "John", "john@gmail.com")
    service_logic.add_user(2, "Jane", "jane@gmail.com")
    service_logic.add_user(3, "Bob", "bob@gmail.com")
    service_logic.add_user(4, "Alice", "alice@gmail.com")

    # Testing groups
    service_logic.make_group(1, "Group 1", [1, 2, 3])
    service_logic.make_group(2, "Group 2", [1, 2, 4])
    service_logic.make_group(3, "Group 3", [1, 2, 3, 4])

    # add expense
    while True:
        group_id = int(input("Enter the group id: "))
        description = input("Enter the description of the expense: ")
        id = int(input("Enter the id of the expense: "))
        creator_id = int(input("Enter the id of the creator of the expense: "))
        amount = int(input("Enter the amount of the expense: "))
        type = int(input("Enter the type of the expense 1: GENERAL or 2: PERCENTAGE: "))
        user_percentages = {}

        if type == 1:
            service_logic.add_expense(id, amount, description, creator_id, group_id)

        elif type == 2:
            for i in service_logic.get_group_members(group_id):
                user_percentages[i] = int(input(f"Enter the percentage of the expense for {i}: "))
            service_logic.add_expense(id, amount, description, creator_id, group_id, 'PERCENTAGE', user_percentages)
        else:
            break




    
