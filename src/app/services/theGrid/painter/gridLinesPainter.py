import tkinter as tk
from src.app.services.theGrid.screenDataExtractor.screenDataExtractor import ScreenDataExtractor
from src.app.services.theGrid.gridInfoStore.gridLinesCoordsStore import GridLinesCoordsStore
from src.app.services.theGrid.gridInfoStore.gridColorKeeper import GridColorKeeper
from src.app.services.theGrid.gridInfoStore.activeRectangleKeeper import ActiveRectangleKeeper
from typing import Tuple, List


class GridLinesPainter:
    def __init__(self):
        self.gridDensity: int = 15
        self.initFullscreenCanvas()
        self.coordsStore = GridLinesCoordsStore()
        self.colorPicker = GridColorKeeper()
        # self.color = "gray15"
        self.color = self.colorPicker.getActiveColor()
        self.activeRectangleKeeper = ActiveRectangleKeeper()

    def initFullscreenCanvas(self) -> None:
        self.maxX, self.maxY = ScreenDataExtractor().getMaxXY()
        options = {
            "width": self.maxX,
            "height": self.maxY,
            # "background": "green",
            "highlightthickness": 0
        }
        self.gridCanvas = tk.Canvas(**options)

    def drawLines(self) -> None:
        self.color = self.colorPicker.getActiveColor()
        self.gridCanvas.delete('all')
        self.coordsStore.calculateAllLinesCoordinates()
        self.drawColumns()
        self.drawRows()
        self._drawActiveRectangle()
        self.gridCanvas.pack()

    def clear(self):
        print("czyszcze!")
        self.gridCanvas.delete('all')
        self.color = "gray20"

        self.drawLines()
        # self.drawRectangle()

    def drawRectangle(self):
        self.gridCanvas.create_line(12, 12, 566, 666, fill="blue")
        self.gridCanvas.pack()

    def _drawActiveRectangle(self):
        self.drawBoldOutlineOnActiveRectangle(8)

    def drawColumns(self):
        verticalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllVertcicalLines()
        lineCoords: Tuple[int, int, int, int]
        for lineCoords in verticalLines:
            self.gridCanvas.create_line(lineCoords, fill=self.color)  # type: ignore

    def drawRows(self):
        horizontalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllHorizontalLines()
        for lineCoords in horizontalLines:
            self.gridCanvas.create_line(lineCoords, fill=self.color)  # type: ignore

    def drawBoldOutlineOnActiveRectangle(self, boldValue: int) -> None:
        rectanglePoints: List[Tuple[int, int]] = self.activeRectangleKeeper.getActiveRectangleCoords()
        rectangleCornerPoint_topLeft: Tuple[int, int] = rectanglePoints[0]
        rectangleCornerPont_topRight: Tuple[int, int] = rectanglePoints[1]
        rectangleCornerPoint_bottomRight: Tuple[int, int] = rectanglePoints[2]
        rectangleCornerPoint_bottomLeft: Tuple[int, int] = rectanglePoints[3]

        for px in range(1, boldValue):
            self.gridCanvas.create_line(
                rectangleCornerPoint_topLeft[0] - px,
                rectangleCornerPoint_topLeft[1] - px,
                rectangleCornerPont_topRight[0] + px,
                rectangleCornerPont_topRight[1] - px,
                fill="green"
            )
            self.gridCanvas.create_line(
                rectangleCornerPont_topRight[0] + px,
                rectangleCornerPont_topRight[1] - px,
                rectangleCornerPoint_bottomRight[0] + px,
                rectangleCornerPoint_bottomRight[1] + px,
                fill="yellow"
            )
            self.gridCanvas.create_line(
                rectangleCornerPoint_bottomRight[0] + px,
                rectangleCornerPoint_bottomRight[1] + px,
                rectangleCornerPoint_bottomLeft[0] - px,
                rectangleCornerPoint_bottomLeft[1] + px,
                fill="red"
            )
            self.gridCanvas.create_line(
                rectangleCornerPoint_bottomLeft[0] - px,
                rectangleCornerPoint_bottomLeft[1] + px,
                rectangleCornerPoint_topLeft[0] - px,
                rectangleCornerPoint_topLeft[1] - px,
                fill="white"
            )
