from app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass
from typing import List
from injector import singleton


@singleton
class GridColorKeeper(metaclass=SingleInstanceMetaClass):
    possibleColors: List[str] = [
        "white",
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
        print("activeColor: " + activeColor)
        return activeColor

    def changeColor(self):
        maxNr: int = len(self.possibleColors) - 1
        self.activeColor_nr += 1
        if self.activeColor_nr > maxNr:
            self.activeColor_nr = 0
        print(f"current color: {self.getActiveColor()}")

    def getParentCellOutlineColor(self):
        color = 'white'
        return color

    def getInnerLinesColor(self):
        color = '#565656'
        return color
