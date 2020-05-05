import Android
import Parse
import os
from pathlib import Path

cwd = os.getcwd()
android = Android.Android((1, 3), Android.Bearing.NORTH, (5,6))
android.LoadInputs(os.path.join(cwd, "instructions.txt"))
