import traceback

from parking_system import ParkingSystem
from vehcile import Vehicle

class ServiceLogic:
    def __init__(self):
        self.__parking_system = ParkingSystem()
        self.__avialable_slots = []

    def create_parking_floor(self, id, floor):
        try:
            self.__parking_system.add_parking_floor(id, floor)
            print("Floor created successfully")
        except Exception as e:
            print(str(e))

    def create_parking_slot(self, id, parking_floor_id):
        try:
            slot = self.__parking_system.add_parking_slot(id, parking_floor_id)
            print("Slot created successfully")
            self.__avialable_slots.append(slot)
        except Exception as e:
            print(str(e))

    def issue_ticket(self, id, vechile):
        if len(self.__avialable_slots) == 0:
            print("No available slots")
            return
        
        slot = self.__avialable_slots.pop()
        try:
            self.__parking_system.create_ticket(id, vechile, slot.get_id())
            print("Ticket issued successfully")
        except Exception as e:
            traceback.print_exc()
            print(str(e))

    def exit_ticket(self, id):
        try:
            slot= self.__parking_system.exit_ticket(id)
            print("Ticket exited successfully")
            self.__avialable_slots.append(slot)
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    service = ServiceLogic()
    print("Welcome to Parking Management System")

    # Hardcoded values for testing
    service.create_parking_floor(1, 1)
    service.create_parking_floor(2, 2)
    service.create_parking_floor(3, 3)

    service.create_parking_slot(1, 1)
    service.create_parking_slot(2, 1)
    service.create_parking_slot(3, 1)
    service.create_parking_slot(4, 2)
    service.create_parking_slot(5, 2)
    service.create_parking_slot(6, 2)
    service.create_parking_slot(7, 3)
    service.create_parking_slot(8, 3)
    service.create_parking_slot(9, 3)

    while True:
        ticket_id = int(input("Enter ticket id: "))
        operation_type = int(input("Enter operation type 1: Issue Ticket, 2: Exit Ticket: "))
        vehicle_type = int(input("Enter vehicle type 1: Bike, 2: Car, 3: Heavy Vehicle, 4: Other: "))

        vechile = None
        if vehicle_type == 1:
            vechile = Vehicle.BIKE
        elif vehicle_type == 2:
            vechile = Vehicle.CAR
        elif vehicle_type == 3:
            vechile = Vehicle.HEAVY_VEHICLE
        elif vehicle_type == 4:
            vechile = Vehicle.OTHER

        if operation_type == 1:
            service.issue_ticket(ticket_id, vechile)
        elif operation_type == 2:
            service.exit_ticket(ticket_id)
        else:
            break
