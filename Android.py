from enum import Enum
from dotmap import DotMap
from dataclasses import dataclass
import json

@dataclass
class Coords:
    x: int
    y: int

@dataclass
class Output:
    type: str
    position: Coords
    bearing: str

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
    MOVEMENT_MAP = { "turn-left" : "LEFT", "turn-right" : "RIGHT", "move-forward" : "FORWARD" }

    @classmethod
    def __init__(self):
        self.position = None
        self.facing = None
        self.area = None

    @classmethod
    def LaunchBot(self, position, facing, area):
        # robot must be positioned on the asteroid
        if position.x > area.x or position.y > area.y:
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
        commands = Android.LoadCommands(location)
        area = commands[0].size
        outCommands = []

        for command in commands:
            if command.type == "new-robot":
                if self.position is not None:
                    outCommands.append(Output("robot", Coords(self.position.x, self.position.y), self.facing))

                self.LaunchBot(Coords(command.position.x, command.position.y), Bearing[command.bearing.upper()], Coords(area.x, area.y))
            if command.type == "move":
                move = self.MOVEMENT_MAP[command.movement]
                self.Move(Movement[move])    

        outCommands.append(Output("robot", Coords(self.position.x, self.position.y), self.facing))
        return outCommands

    @classmethod
    def LoadCommands(self, location):
        commands = []

        with open(location, 'r') as input:
            for line in input:
                command = json.loads(line)
                commands.append(DotMap(command))

        if commands[0].type != "asteroid":
            ValueError("First command must define the asteroid")

        if commands[1].type != "new-robot":
            ValueError("Sedond command must define an android")

        return commands

    @classmethod
    def Move(self, movement):
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            Android.Rotate(movement)
        elif movement == Movement.FORWARD:
            Android.ForwardMove()

    @classmethod
    def Rotate(self, movement):
        turns = [4, 1, 2, 3, 4, 1] # create a list of valid directions that wraps around
        result = self.facing.value + movement.value
        result = turns[result]
        self.facing = Bearing(result)

    @classmethod
    def ForwardMove(self):
        x = self.position.x + self.MOVEMENT[self.facing].x
        y = self.position.y + self.MOVEMENT[self.facing].y

        if self.CheckBounds(x, y):
            self.position.x = x
            self.position.y = y
        else:
            raise ValueError()
    
    @classmethod
    def CheckBounds(self, x, y):
        valid = True
        if x > self.area.x or y > self.area.y:
            valid = False

        if x < 0 or y < 0:
            valid = False

        return valid
    

