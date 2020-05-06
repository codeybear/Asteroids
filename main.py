import Android
import os
from pathlib import Path

cwd = os.getcwd()
android = Android.Android((1, 3), Android.Bearing.NORTH, (5,6))
android.RunCommandsFromFile(os.path.join(cwd, "instructions.txt"))
