from elevator_system import ElevatorSystem
from direction import Direction

class ServiceLogic:
    def __init__(self, floors, lifts_count):
        self.__elevator_system = ElevatorSystem(floors, lifts_count)


    def call_elevator(self, direction, floor):
        return self.__elevator_system.assign_elevator(floor, direction)
    
    def add_request(self, elevator, floor):
        self.__elevator_system.add_request(elevator, floor)

    def get_elevator(self, elevator_id):
        return self.__elevator_system.get_elevator(elevator_id)
    
    def get_all_elevators(self):
        return self.__elevator_system.get_all_elevators()

    def move_elevator(self, elevator):
        self.__elevator_system.move_elevator(elevator)

    def main_logic(self):
        while True:
            floor = int(input("Enter the floor: "))
            direction_input = int(input("Enter the direction 1: up 2: down: "))
            direction = Direction.UP if direction_input == 1 else Direction.DOWN

            request_type = int(input("Enter the request type 1: inside 2: outside: "))

            if request_type == 2:
                elevator = self.call_elevator(direction, floor) # assigning the elevator
            
            elif request_type == 1:
                id = int(input("Enter the elevator id: "))
                elevator = self.get_elevator(id)
                self.add_request(elevator, floor)

            else:
                print("Invalid request type")
                break

            for elevator in self.get_all_elevators().values():
                self.move_elevator(elevator)


if __name__ == "__main__":

    # Elevator System for 5 floors and 3 lifts
    service = ServiceLogic(5, 2)

    print("Welcome to Elevator Management System")
    print("For this system currently we have 2 elevators and 5 floors")

    service.main_logic()
