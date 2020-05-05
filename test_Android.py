import pytest
import Android

def test_Instantiate():
    android = Android.Android((1, 3), Android.Bearing.NORTH, (5,6))
    assert android.area == (5,6)
    
def test_Instantiate_invalid_params():
    with pytest.raises(ValueError):
        Android.Android((7, 9), Android.Bearing.NORTH, (5,6))
    
