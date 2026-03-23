from elevator import Elevator
from direction import Direction

class ElevatorSystem:
    def __init__(self, floors, elevators_count):
        self.__floors = floors
        self.__elevators_count = elevators_count

        self.__elevators = {}
        self.__requests = {}

        for i in range(self.__elevators_count):
            self.__elevators[i] = Elevator(i, self.__floors)
            self.__requests[i] = set()

        print(f"Elevators are {self.__elevators}")
        print(f"Requests are {self.__requests}")


    def assign_elevator(self, floor, direction):
        for elevator in self.__elevators.values():
            if elevator.get_current_floor() == floor:
                return elevator
            
        mini_diff = 99999
        assigned_elevator = None

        for elevator in self.__elevators.values():
            current_elevator_floor = elevator.get_current_floor()
            current_elevator_direction = elevator.get_direction()
            elevator_request_set = self.__requests[elevator.get_id()]

            if current_elevator_direction == Direction.UP:
                if direction == Direction.UP:
                    if floor > current_elevator_floor or len(elevator_request_set) == 0:
                        diff = abs(floor - current_elevator_floor)
                    else:
                        diff = abs(max(elevator_request_set) - current_elevator_floor)+abs(floor - max(elevator_request_set))
                else:
                    if len(elevator_request_set) ==  0:
                        diff = abs(floor - current_elevator_floor)
                    else:
                        diff = abs(max(elevator_request_set) - current_elevator_floor)+abs(floor - max(elevator_request_set))

            if current_elevator_direction == Direction.DOWN:
                if direction == Direction.DOWN:
                    if floor < current_elevator_floor or len(elevator_request_set) == 0:
                        diff = abs(floor - current_elevator_floor)
                    else:
                        diff = abs(min(elevator_request_set) - current_elevator_floor)+abs(floor - min(elevator_request_set))
                else:
                    if len(elevator_request_set) ==  0:
                        diff = abs(floor - current_elevator_floor)
                    else:
                        diff = abs(min(elevator_request_set) - current_elevator_floor)+abs(floor - min(elevator_request_set))

            if current_elevator_direction is None:
                diff = abs(floor - current_elevator_floor)
                
            if mini_diff > diff:
                mini_diff = diff
                assigned_elevator = elevator

            
        self.__requests[assigned_elevator.get_id()].add(floor)
        print(f"Assigned elevator {assigned_elevator.get_id()} to floor {floor}")

        return assigned_elevator

    def add_request(self, elevator, floor):        
        self.__requests[elevator.get_id()].add(floor)
        print(f"Assigned elevator {elevator.get_id()} to floor {floor}")

    def get_elevator(self, elevator_id):
        return self.__elevators[elevator_id]
    
    def get_all_elevators(self):
        return self.__elevators
    
    def direction_handling(self, elevator):
        direction = elevator.get_direction()
        if direction is None:

            if elevator.get_current_floor() > max(self.__requests[elevator.get_id()]):
                print("Elevator moving down")
                direction = Direction.DOWN

            if elevator.get_current_floor() < min(self.__requests[elevator.get_id()]):
                print("Elevator moving up")
                direction = Direction.UP

        else:
            if direction == Direction.UP and elevator.get_current_floor() > max(self.__requests[elevator.get_id()]):
                print("Elevator moving down")
                direction = Direction.DOWN

            if direction == Direction.DOWN and elevator.get_current_floor() < min(self.__requests[elevator.get_id()]):
                print("Elevator moving up")
                direction = Direction.UP

        return direction


    def move_elevator(self, elevator):
        if len(self.__requests[elevator.get_id()]) == 0:
            elevator.set_direction(None)
            print("Halted due to no requests")
            return
        
        direction = self.direction_handling(elevator)

        elevator.move_one_floor(direction)

        if elevator.get_current_floor() in self.__requests[elevator.get_id()]:
            self.__requests[elevator.get_id()].remove(elevator.get_current_floor())
            print("Halted in the floor")
            return

        elevator.set_direction(direction)

