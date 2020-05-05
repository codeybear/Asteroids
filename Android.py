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
    # TODO convert to a dict and lookup by Bearing
    MOVE_NORTH = (0, 1)
    MOVE_EAST = (1, 0)
    MOVE_SOUTH = (0, -1)
    MOVE_WEST = (-1, 0)

    MOVEMENT = {}

    # def __init__(self, position, facing, area):

    @classmethod
    def LaunchBot(self, position, facing, area):
        # robot must be positioned on the asteroid
        if position.x >= area.x or position.y >= area.y:
            raise ValueError()

        self.position = position
        self.facing = facing
        self.area = area

    def RunInstructions(self, location):
        commands = LoadInputs(location)
        for command in commands:
            RunCommand(command)

    # def RunCommand(self, command):
    #     pass

    @classmethod
    def RunCommandsFromFile(self, location):
        commands = []

        with open(location, 'r') as input:
            for line in input:
                command = json.loads(line)
                commands.append(DotMap(command))
        
        return commands

    def Move(self, movement):
        # TODO move functions should be smaller
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            # moves = [range(5)]
            result = self.facing.value + movement.value
            if result == 0: result = 4
            if result == 5: result = 1
            self.facing = Bearing(result)
        elif movement == Movement.FORWARD:
            self.position[0] += movement
            self.position[1] += movement
        