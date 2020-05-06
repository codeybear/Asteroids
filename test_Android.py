import pytest
import Android
import os

cwd = os.getcwd()
path = os.path.join(cwd, "instructions.txt")

def test_Instantiate():
    android = Android.Android()
    android.LaunchBot(Android.Coords(1, 3), Android.Bearing.NORTH, Android.Coords(5,6))
    assert android.area == Android.Coords(5,6)
    
def test_Instantiate_invalid_params():
    android = Android.Android()

    with pytest.raises(ValueError):
        android.LaunchBot(Android.Coords(5, 6), Android.Bearing.NORTH, Android.Coords(4,5))
    
def test_RunCommandsFromFile():
    android = Android.Android()
    commands = android.RunCommandsFromFile(path)
    assert commands[0].position.x == 1 and commands[0].position.y == 3 and commands[1].position.x == 5 and commands[1].position.y == 1
    
def test_MoveForwardValidNorth():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.FORWARD)
    assert android.position == Android.Coords(2, 3)

def test_MoveForwardValidEast():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.EAST, Android.Coords(6,6))
    android.Move(Android.Movement.FORWARD)
    assert android.position == Android.Coords(3, 2)

def test_MoveForwardInvalidTop():
    android = Android.Android()
    android.LaunchBot(Android.Coords(0, 5), Android.Bearing.NORTH, Android.Coords(5,5))
    with pytest.raises(ValueError):
        android.Move(Android.Movement.FORWARD)

def test_MoveForwardInvalidBottom():
    android = Android.Android()
    android.LaunchBot(Android.Coords(0, 0), Android.Bearing.SOUTH, Android.Coords(6,6))
    with pytest.raises(ValueError):
        android.Move(Android.Movement.FORWARD)

def test_MoveForwardInvalidEast():
    android = Android.Android()
    android.LaunchBot(Android.Coords(5, 0), Android.Bearing.EAST, Android.Coords(5, 5))
    with pytest.raises(ValueError):
        android.Move(Android.Movement.FORWARD)

def test_TurnLeftValid():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.LEFT)
    assert android.facing == Android.Bearing.WEST

def test_TurnRightValid():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.RIGHT)
    assert android.facing == Android.Bearing.EAST
