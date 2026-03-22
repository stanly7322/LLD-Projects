from status import SlotStatus

class ParkingSlot:
    def __init__(self, id, parking_floor, status = SlotStatus.AVAILABLE):
        self.__id = id
        self.__parking_floor = parking_floor
        self.__status = status
        
    def get_id(self):
        return self.__id
    
    def get_parking_floor(self):
        return self.__parking_floor
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
        