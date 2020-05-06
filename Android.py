from enum import Enum
from dotmap import DotMap
from dataclasses import dataclass
import json

@dataclass
class Coords:
    x: int
    y: int

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
    # movement in the x and y direction for each of the bearings
    MOVEMENT = {Bearing.NORTH : Coords(0, 1), Bearing.EAST : Coords(1, 0), Bearing.SOUTH : Coords(0, -1), Bearing.WEST : Coords(-1, 0)} 

    @classmethod
    def LaunchBot(self, position, facing, area):
        # robot must be positioned on the asteroid
        if position.x >= area.x or position.y >= area.y:
            raise ValueError()

        self.position = position
        self.facing = facing
        self.area = area

    @classmethod
    def RunInstructions(self, location):
        commands = LoadInputs(location)
        for command in commands:
            RunCommand(command)

    @classmethod
    def RunCommandsFromFile(self, location):
        commands = []

        with open(location, 'r') as input:
            for line in input:
                command = json.loads(line)
                commands.append(DotMap(command))
        
        return commands

    @classmethod
    def Move(self, movement):
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            turns = [4, 1, 2, 3, 4, 1] # create a list of valid directions that wraps around
            result = self.facing.value + movement.value
            result = turns[result]
            self.facing = Bearing(result)
        elif movement == Movement.FORWARD:
            x = self.position.x + self.MOVEMENT[self.facing.value].x
            y = self.position.y + self.MOVEMENT[self.facing.value].y

            if x < self.area.x and y < self.area.y:
                self.position.x = x
                self.position.y = y
            else:
                raise ValueError()