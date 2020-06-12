from enum import Enum
from dotmap import DotMap
from dataclasses import dataclass
import jsons
import os

@dataclass
class Coords:
    x: int
    y: int

# output structure
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
    # mappings from JSON to Bearing Enum
    MOVEMENT_MAP = { "turn-left" : "LEFT", "turn-right" : "RIGHT", "move-forward" : "FORWARD" }

    def __init__(self):
        self.position = None
        self.facing = None
        self.area = None

    def LaunchBot(self, position, facing, area):
        # robot must be positioned on the asteroid
        if position.x > area.x or position.y > area.y:
            raise ValueError()

        self.position = position
        self.facing = facing
        self.area = area

    def RunCommandsFromFile(self, location):
        ### Load and run files from valid JSON file ###
        commands = self.LoadCommands(location)
        area = commands[0].size
        outCommands = []

        for command in commands:
            if command.type == "new-robot":
                if self.position is not None:   # store the final position of the android
                    outCommands.append(Output("robot", Coords(self.position.x, self.position.y), self.facing))

                self.LaunchBot(Coords(command.position.x, command.position.y), Bearing[command.bearing.upper()], Coords(area.x, area.y))
            if command.type == "move":
                move = self.MOVEMENT_MAP[command.movement]
                self.Move(Movement[move])    

        outCommands.append(Output("robot", Coords(self.position.x, self.position.y), self.facing))
        return outCommands

    def SendOutput(self, commands):
        """ Send final robot positions to output """
        output = ""

        for command in commands:
            output += jsons.dumps(command) + os.linesep

        output = output.replace("Bearing.", "").lower()
        print(output)

    def LoadCommands(self, location):
        """ Load commands from specified JSON file """
        commands = []

        with open(location, 'r') as input:
            for line in input:
                command = jsons.loads(line)
                commands.append(DotMap(command))

        if commands[0].type != "asteroid":
            ValueError("First command must define the asteroid")

        if commands[1].type != "new-robot":
            ValueError("Second command must define an android")

        return commands

    def Move(self, movement):
        if movement == Movement.RIGHT or movement == Movement.LEFT:
            self.Rotate(movement)
        elif movement == Movement.FORWARD:
            self.ForwardMove()

    def Rotate(self, movement):
        turns = [4, 1, 2, 3, 4, 1] # create a list of valid bearings that wraps around
        result = self.facing.value + movement.value
        result = turns[result]
        self.facing = Bearing(result)

    def ForwardMove(self):
        x = self.position.x + self.MOVEMENT[self.facing].x
        y = self.position.y + self.MOVEMENT[self.facing].y

        if self.CheckBounds(x, y):  
            self.position.x = x
            self.position.y = y
        else:
            raise ValueError()
    
    def CheckBounds(self, x, y):
        """ make sure the position is within the bounds of the asteroid """
        valid = True
        if x > self.area.x or y > self.area.y:
            valid = False

        if x < 0 or y < 0:
            valid = False

        return valid
    

