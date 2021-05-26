# from abc import metaclass
from src.app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass
from src.app.services.theGrid.screenDataExtractor.screenDataExtractor import ScreenDataExtractor
from typing import List, Tuple


class GridLinesCoordsStore(metaclass=SingleInstanceMetaClass):
    # class GridLinesCoordsStore():
    def __init__(self):
        self.density = 15
        self.calculateAllLinesCoordinates()
        pass

    def setCurrentRectangleCoords(self, x1, y1, x2, y2):
        pass

    def getAllVertcicalLines(self) -> List[Tuple[int, int, int, int]]:
        return self.verticalLines

    def getAllHorizontalLines(self) -> List[Tuple[int, int, int, int]]:
        return self.horizontalLines

    def setGridDensity(self, density: int):
        self.density = density
        self.calculateAllLinesCoordinates()

    def incGridDensity(self, step: int = 1):
        # if self.density > 1:
        self.density += step

    def decGridDensity(self, step: int = 1):
        if self.density > 1:
            self.density -= step
        else:
            print(f"Minimum density has been reached: {self.density}. I can't decrease it.")

    def calculateAllLinesCoordinates(self):
        self._getScreenSizes()
        self._calcVerticalLinesCoords()
        self._calcHorizontalLinesCoords()

    def _getScreenSizes(self):
        self.screen_maxX, self.screen_maxY = ScreenDataExtractor().getMaxXY()

    def _calcVerticalLinesCoords(self) -> None:
        spaceBetweenLines: int = self.screen_maxX // self.density
        line_xPos: int = 0
        self.verticalLines: List[Tuple[int, int, int, int]] = []

        while line_xPos <= self.screen_maxX:
            point1: Tuple[int, int] = line_xPos, 0
            point2: Tuple[int, int] = line_xPos, self.screen_maxY
            currentLine: Tuple[int, int, int, int] = point1 + point2
            self.verticalLines.append(currentLine)

            line_xPos += spaceBetweenLines

    def _calcHorizontalLinesCoords(self) -> None:
        spaceBetweenLines: int = self.screen_maxY // self.density
        line_yPos: int = 0
        self.horizontalLines: List[Tuple[int, int, int, int]] = []

        while line_yPos <= self.screen_maxY:
            point1: Tuple[int, int] = 0, line_yPos
            point2: Tuple[int, int] = self.screen_maxX, line_yPos
            currentLine: Tuple[int, int, int, int] = point1 + point2
            self.horizontalLines.append(currentLine)

            line_yPos += spaceBetweenLines
