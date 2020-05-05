import pytest
import Android

def test_Instantiate():
    android = Android.Android((1, 3), Android.Bearing.NORTH, (5,6))
    assert android.area == (5,6)
    
def test_Instantiate_invalid_params():
    with pytest.raises(ValueError):
        Android.Android((5, 6), Android.Bearing.NORTH, (5,6))
    
def test_LoadInput_CheckForAsteroid():
    commands = Parse.LoadInputs(os.path.join(cwd, "instructions.txt"))
    command = command[0]
    assert command.type == "asteroid"
