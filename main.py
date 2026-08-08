from enum import Enum
import time
import subprocess

class CompassDirections(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"

def ClearConsole():
    subprocess.run("cls", shell=True)

def TypeToConsole(string, delay=0.05):

    for letter in string:
        time.sleep(delay)
        print(letter, end="", flush=True)

    return

ClearConsole()

ProgramRunning = True

while ProgramRunning:

    TypeToConsole("ROOMS\n\n1 - New Game\n2 - Load Game\n3 - About Me\n4 - Exit\n\n")
    MainMenuUserChoice = input()

    if MainMenuUserChoice == "1":
        pass
    elif MainMenuUserChoice == "2":
        pass
    elif MainMenuUserChoice == "3":
        ClearConsole()
        TypeToConsole("ABOUT ME:\n\n")
        TypeToConsole("Welcome to ROOMS, a text-based adventure game I made in Year 9.\n")
        TypeToConsole("At the time I didn\'t know how to write clean code, so looking back now I couldn\'t bear to show this code to employers.\n")
        TypeToConsole("As a result, I've decided to spend some of my Year 12 Summer Holiday Revisiting this game.\n")
        TypeToConsole("If you want to see how poorly written the code was check out the past commits on GitHub, it will be the first commit.\n")
        TypeToConsole("\nhttps://github.com/DoomSlayer350\n\n")
        TypeToConsole("Now that we got that little brief out the way, how about I introduce the game now.\n")
        TypeToConsole("[ADD GAME INTRO HERE]")
        time.sleep(1.5)
        input("\n\n[PRESS ENTER TO ESCAPE]\n\n")
        ClearConsole()
    elif MainMenuUserChoice == "4":
        ClearConsole()
        TypeToConsole("EXITING...")
        time.sleep(1)
        ClearConsole()
        ProgramRunning = False
    else:
        ClearConsole()
        TypeToConsole("INVALID CHOICE USER...", 0.2)
        time.sleep(2)
        ClearConsole()