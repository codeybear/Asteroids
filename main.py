import Android
import Parse
import os
from pathlib import Path

cwd = os.getcwd()
commands = Parse.LoadInputs(os.path.join(cwd, "instructions.txt"))
#android = Android.Android((1, 3), Android.Bearing.NORTH, (5,6))
