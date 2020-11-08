import tkinter as tk
from typing import Tuple, List
from injector import singleton, inject
from app.services.theGrid.screenDataExtractor.screenDataExtractor import ScreenDataExtractor
from app.services.theGrid.gridInfoStore.gridColorKeeper import GridColorKeeper
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper
from app.services.kwargsKeeper.kwargsKeeper import KwKeeper
from app.modes.models.rectangle import Rectangle
from app.modes.focuser.service.cellsPositionCalculator import CellsPositionCalculator
from app.modes.models.enums.innerPartRelativePosition import InnerPartRelativePosition_enum
from app.services.mouseHandler.mouseHandler import MouseHandler
from app.modes.focuser.service.cellMidFinder import CellMidFinder
from app.modes.models.point import Point
from app.services.theGrid.windowSetter.canvasInstanceKeeper import CanvasInstanceKeeper
from app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller
from app.modes.focuser.service.cellInnerCrossMaker import CellInnerCrossMaker
from app.modes.focuser.service.historyKeeper import HistoryKeeper


@singleton
class Focuser:
    @inject
    def __init__(self,
                 windowInstanceKeeper: WindowInstanceKeeper,
                 screenDataExtractor: ScreenDataExtractor,
                 gridColorKeeper: GridColorKeeper,
                 cellsPositionCalculator: CellsPositionCalculator,
                 cellMidFinder: CellMidFinder,
                 mouseHandler: MouseHandler,
                 canvasInstanceKeeper: CanvasInstanceKeeper,
                 windowActionsCaller: WindowActionsCaller,
                 cellInnerCrossMaker: CellInnerCrossMaker,
                 historyKeeper: HistoryKeeper,
                 ):
        self.windowActionsCaller = windowActionsCaller
        self.screenDataExtractor = screenDataExtractor
        self.gridWindow: tk.Tk = windowInstanceKeeper.getWindow()
        self.canvasInstanceKeeper = canvasInstanceKeeper
        self.colorKeeper = gridColorKeeper
        self.cellsPositionCalculator = cellsPositionCalculator
        self.cellMidFinder = cellMidFinder
        self.mouseHandler = mouseHandler
        self.cellInnerCrossMaker = cellInnerCrossMaker
        self.historyKeeper = historyKeeper

    def showMe(self):
        self._bindBasicKeys()
        # self.__setRootCell()
        self.__drawRootCellLines()

    def __drawRootCellLines(self):
        maxX, maxY = self.screenDataExtractor.getMaxXY()
        maxCell: Rectangle = Rectangle(0, 0, width=maxX, height=maxY)
        self.canvas = self.canvasInstanceKeeper.getCanvas()
        self.__drawCell(maxCell)
        self.historyKeeper.setRootCell(maxCell)

    def __clearCanvas(self):
        self.canvas.delete('all')

    def _bindBasicKeys(self) -> None:
        goDirection = InnerPartRelativePosition_enum
        self.gridWindow.bind('w', lambda _: self.__handleBindedKeyPress(goDirection.topLeft))
        self.gridWindow.bind('s', lambda _: self.__handleBindedKeyPress(goDirection.botLeft))
        self.gridWindow.bind('e', lambda _: self.__handleBindedKeyPress(goDirection.topRight))
        self.gridWindow.bind('d', lambda _: self.__handleBindedKeyPress(goDirection.botRight))
        self.gridWindow.bind('g', lambda _: self.__moveToCurrentCell())
        # self.gridWindow.bind(['g', 'c'], lambda _: self.__moveToAndClickCurrentCell())
        self.gridWindow.bind('c', lambda _: self.__moveToAndClickCurrentCell())
        self.gridWindow.bind('r', lambda _: self.__goBackInHistory())

    def __moveToAndClickCurrentCell(self) -> None:
        print("click!")
        self.__moveToCurrentCell()
        self.windowActionsCaller.hideWindow()
        self.__clickInCellCenter(self.currentCell)
        self.__drawInitialScreen()

    def __drawInitialScreen(self) -> None:
        rootCell = self.historyKeeper.getRootCell()
        self.__drawCell(rootCell)
        self.historyKeeper.clearHistory()
        print(f"draw initial screen: {rootCell}")

    def __clickInCellCenter(self, cell: Rectangle) -> None:
        self.__moveToCurrentCell()
        self.mouseHandler.click()

    def __moveToCurrentCell(self) -> None:
        midPoint: Point = self.cellMidFinder.findMidPoint(self.currentCell)
        print(f"(moving-to-center) Mid point: {midPoint}")
        self.mouseHandler.moveMouseToPoint(midPoint)

    def __handleBindedKeyPress(self, goDirection: InnerPartRelativePosition_enum):
        self.__focusOnCell(goDirection)

    def __focusOnCell(self, zoomDirection: InnerPartRelativePosition_enum):
        print("direction picked: " + zoomDirection)
        self.__focusToCell(zoomDirection)
        # self.historyKeeper.

    def __focusToCell(self, zoomDirection: InnerPartRelativePosition_enum):
        newCell: Rectangle = self.cellsPositionCalculator.calcNewPosition(self.currentCell, zoomDirection)
        self.__drawCell(newCell)

    def __drawCell(self, cell: Rectangle, goingBack: bool = False):
        self.__clearCanvas()
        color = self.colorKeeper.getParentCellOutlineColor()
        self.canvas.create_rectangle(*cell, outline=color)
        print(f"Rysuję: {cell}")
        self.cellInnerCrossMaker.drawPartisionLines(cell)
        self.__setCurrentCell(cell, goingBack)

    def __setCurrentCell(self, newCell, goingBack: bool = False):
        self.currentCell = newCell
        if not goingBack:
            self.historyKeeper.rememberMove(newCell)
        # self.historyKeeper.removeUndoneMovesFromHistory()

    def __goBackInHistory(self):
        print("Attempt to undo last focus move.")
        # cellToDraw: Rectangle = self.historyKeeper.getLastMove()
        cellToDraw: Rectangle = self.historyKeeper.getOlderMove()
        self.__drawCell(cellToDraw, goingBack=True)
