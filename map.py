import random
from room import Room
import numpy

def AddNewRoomToEachCoordinate(Map, MapSize):
    for YCoordinate in range(0, MapSize["y"]):
        print((Map[YCoordinate]))
        for XCoordinate in range(0, MapSize["x"]):
            print("Coordinates: ",XCoordinate, YCoordinate)
            print((Map[YCoordinate][XCoordinate]))
            Map[YCoordinate][XCoordinate] = Room({"x": XCoordinate, "y": YCoordinate}, None, None)


def GenerateMap():
    MapSize = {"x": random.randint(6,16), "y": random.randint(6,16)}
    print(MapSize)
    Map = numpy.full((MapSize["y"], MapSize["x"]), Room(None, None, None))
    #Map = numpy.zeros((MapSize["y"], MapSize["x"]))
    print(Map)
    AddNewRoomToEachCoordinate(Map, MapSize)
    print(Map)

GenerateMap()