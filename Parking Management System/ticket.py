from status import TicketStatus


class Ticket:
    def __init__(self, id, vechile, parking_slot, status = TicketStatus.VALID):
        self.__id = id
        self.__vehicle = vechile
        self.__parking_slot = parking_slot
        self.__status = status

    def get_id(self):
        return self.__id
    
    def get_vehicle(self):
        return self.__vehicle
    
    def get_parking_slot(self):
        return self.__parking_slot
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status