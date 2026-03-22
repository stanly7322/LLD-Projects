from parking_floor import ParkingFloor
from parking_slot import ParkingSlot
from ticket import Ticket
from vehcile import Vehicle
from status import SlotStatus, TicketStatus

class ParkingSystem:
    def __init__(self):
        self.__parking_floors = {}
        self.__parking_slots = {}
        self.__tickets = {}

    def add_parking_floor(self, id, floor):
        if id in self.__parking_floors:
            raise Exception("Floor already exists")
        
        self.__parking_floors[id] = ParkingFloor(id, floor)
        print(f"Current floors are : {self.__parking_floors}")

    def get_parking_floor(self, id):
        return self.__parking_floors.get(id, None)
    
    def add_parking_slot(self, id, parking_floor_id):
        if id in self.__parking_slots:
            raise Exception("Slot already exists")
        
        parking_floor = self.get_parking_floor(parking_floor_id)
        if not parking_floor:
            raise Exception("Floor does not exist")
        
        self.__parking_slots[id] = ParkingSlot(id, parking_floor)
        print(f"Current slots are : {self.__parking_slots}")
        return self.__parking_slots[id]
        

    def get_parking_slot(self, id):
        return self.__parking_slots.get(id, None)
    
    def create_ticket(self, id, vehicle, parking_slot_id):
        if id in self.__tickets:
            raise Exception("Ticket already exists")
        
        parking_slot = self.get_parking_slot(parking_slot_id)
        if not parking_slot:
            raise Exception("Parking slot does not exist")
        
        if parking_slot.get_status() == SlotStatus.OCCUPIED:
            raise Exception("Parking slot is occupied")
        
        self.__tickets[id] = Ticket(id, vehicle, parking_slot)
        parking_slot.set_status(SlotStatus.OCCUPIED)
        self.__parking_slots[parking_slot_id] = parking_slot
        

    def exit_ticket(self, id):
        ticket = self.__tickets.get(id, None)
        if not ticket:
            raise Exception("Ticket does not exist")
        
        parking_slot = ticket.get_parking_slot()

        if ticket.get_status() == TicketStatus.VALID:
            ticket.set_status(TicketStatus.EXPIRED)
            parking_slot.set_status(SlotStatus.AVAILABLE)
        else:
            raise Exception("Ticket is not valid")
        
        self.__tickets[id] = ticket
        self.__parking_slots[parking_slot.get_id()] = parking_slot
        return parking_slot


    def get_ticket(self, id):
        return self.__tickets.get(id, None)



