from enum import Enum
import os
import time
import subprocess

class CompassDirections(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"

SomeDirection = CompassDirections.North

print(SomeDirection)
time.sleep(1)
subprocess.run("cls", shell=True)