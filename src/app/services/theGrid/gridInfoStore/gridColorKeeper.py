from app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass
from typing import List


class GridColorKeeper(metaclass=SingleInstanceMetaClass):
    possibleColors: List[str] = [
        "gray1",
        "gray9",
        "gray19",
        "gray29",
        "blue",
        "green",
        "white",
        "yellow",
    ]
    activeColor_nr: int = 0

    def __init__(self):
        pass

    def getActiveColor(self) -> str:
        activeColor: str = self.possibleColors[self.activeColor_nr]
        return activeColor

    def changeColor(self):
        maxNr: int = len(self.possibleColors) - 1
        self.activeColor_nr += 1
        if self.activeColor_nr > maxNr:
            self.activeColor_nr = 0
        print(f"current color: {self.getActiveColor()}")
