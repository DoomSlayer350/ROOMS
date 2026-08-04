from enum import Enum
import time
import subprocess
import time

class CompassDirections(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"

def ClearConsole():
    subprocess.run("cls", shell=True)

def TypeToConsole(string, delay):

    for letter in string:
        time.sleep(delay)
        print(letter, end="", flush=True)

    print("\n")
    return

ClearConsole()
TypeToConsole("Hey wassamata you altair", 0.1)