from enum import Enum

class SlotStatus(Enum):
    AVAILABLE = (1, "Available")
    OCCUPIED = (2, "Occupied")
    UNDER_MAINTENANCE = (3, "Under Maintenance")

class TicketStatus(Enum):
    VALID = (1, "Valid")
    INVALID = (2, "Invalid")
    EXPIRED = (3, "Expired")
