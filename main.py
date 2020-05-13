import Android
import os
from pathlib import Path

cwd = os.getcwd()
path = os.path.join(cwd, "instructions.txt")
android = Android.Android()
commands = android.RunCommandsFromFile(path)
android.SendOutput(commands)
