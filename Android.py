from enum import Enum
from dotmap import DotMap
import json

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
        if position[0] >= area[0] or position[1] >= area[1] :
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
            self.facing += movement
            if self.facing == 0: self.facing == Bearing.WEST
            if self.facing == 5: self.facing == Bearing.EAST
        elif movement == Movement.FORWARD:
            self.position[0] += MOVEMENT[movement][0]
            self.position[2] += MOVEMENT[movement][1]
        