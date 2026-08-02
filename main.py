from enum import Enum

class CompassDirections(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"

SomeDirection = CompassDirections.North

print(SomeDirection)