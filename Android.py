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
    # tuples could really be coords
    MOVEMENT = {1 : (0, 1), 2 : (1, 0), 3 : (0, -1), 4 : (-1, 0)} 

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

    @classmethod
    def RunCommandsFromFile(self, location):
        commands = []

        with open(location, 'r') as input:
            for line in input:
                command = json.loads(line)
                commands.append(DotMap(command))
        
        return commands

    def Move(self, movement):
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            result = self.facing.value + movement.value
            if result == 0: result = 4
            if result == 5: result = 1
            self.facing = Bearing(result)
        elif movement == Movement.FORWARD:
            x = self.position.x + self.MOVEMENT[self.facing.value][0]
            y = self.position.y + self.MOVEMENT[self.facing.value][1]

            if x < self.area.x or y < self.area.y:
                self.position.x = x
                self.position.y = y