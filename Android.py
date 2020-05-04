from enum import Enum

class Movement(Enum):
    LEFT = 1
    RIGHT = 2
    FORWARD = 3

class Bearing(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class Android:
    def __init__(self, x, y, facing):
        self.position = (x, y)
        self.facing = facing

    def Land(self):
        pass

    def Turn(self):
        pass

    def Move(self):
        pass

        