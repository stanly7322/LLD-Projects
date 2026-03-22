from enum import Enum


class Vehicle(Enum):
    BIKE = (1, "Bike")
    CAR = (2, "Car")
    HEAVY_VEHICLE = (3, "Heavy Vehicle")
    OTHER = (4, "Other")