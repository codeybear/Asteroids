import pytest
import Android
import os

def test_Instantiate():
    android = Android.Android()
    android.LaunchBot(Android.Coords(1, 3), Android.Bearing.NORTH, Android.Coords(5,6))
    assert android.area == Android.Coords(5,6)
    
def test_Instantiate_invalid_params():
    android = Android.Android()

    with pytest.raises(ValueError):
        android.LaunchBot(Android.Coords(5, 6), Android.Bearing.NORTH, Android.Coords(5,6))
    
def test_LoadInput_CheckForAsteroid():
    android = Android.Android()
    cwd = os.getcwd()
    commands = android.RunCommandsFromFile(os.path.join(cwd, "instructions.txt"))
    command = commands[0]
    assert command.type == "asteroid"

def test_MoveForwardValid():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.FORWARD)
    assert android.position == Android.Coords(2, 3)

def test_MoveLeftValid():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.LEFT)
    assert android.facing == Android.Bearing.WEST

def test_MoveRightValid():
    android = Android.Android()
    android.LaunchBot(Android.Coords(2, 2), Android.Bearing.NORTH, Android.Coords(6,6))
    android.Move(Android.Movement.RIGHT)
    assert android.facing == Android.Bearing.EAST