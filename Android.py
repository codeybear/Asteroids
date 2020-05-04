from enum import Enum

class Movement(Enum):
    LEFT = -1
    RIGHT = 1
    FORWARD = 2

class Bearing(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Android:
    def __init__(self, position, facing, area):
        self.position = position
        self.facing = facing
        self.area = area

    def Turn(self, movement):
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            self.facing += movement
            if self.facing == 0: self.facing == Bearing.WEST
            if self.facing == 5: self.facing == Bearing.EAST
        elif movement == Movement.FORWARD:
            pass

    def Move(self):
        pass

        