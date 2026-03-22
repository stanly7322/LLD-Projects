from enum import Enum

class Status(Enum):
    AVAILABLE = (1, "Available")
    BORROWED = (2, "Borrowed")