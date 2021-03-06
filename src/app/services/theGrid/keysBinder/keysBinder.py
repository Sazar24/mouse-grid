import tkinter as tk
from typing import Callable

from src.app.services.theGrid.painter.gridLinesPainter import GridLinesPainter
from src.app.services.theGrid.gridInfoStore.gridLinesCoordsStore import GridLinesCoordsStore
from src.app.services.theGrid.gridInfoStore.gridColorKeeper import GridColorKeeper
from src.app.services.theGrid.gridInfoStore.activeRectangleKeeper import ActiveRectangleKeeper
from src.app.services.mouseEmulator.mouseEventsCreator import MouseEventsCreator
from src.app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller


class KeysBinder:
    def __init__(self, linesPainter: GridLinesPainter, tkWindow: tk.Tk):
        self.linesPainter: GridLinesPainter = linesPainter
        self.gridWindow: tk.Tk = tkWindow
        self._bindBasicKeys()
        self.coordsStore = GridLinesCoordsStore()
        self.colorPicker = GridColorKeeper()
        self.activeRectangleKeeper = ActiveRectangleKeeper()
        self.mouseEventsCreator = MouseEventsCreator()
        self.windowActionsCaller = WindowActionsCaller(tkWindow)

    def _bindBasicKeys(self) -> None:
        self.gridWindow.bind('<Escape>', lambda _: self.gridWindow.destroy())
        self.gridWindow.bind('<Control-p>', lambda _: print("ctrl-p pressed"))
        self.gridWindow.bind('S', lambda _: print("S - pressed"))
        self.gridWindow.bind("<Control-Shift-I>", lambda _: self._moreSquares())
        self.gridWindow.bind("<Control-Shift-K>", lambda _: self._lessSquares())
        self.gridWindow.bind("n", lambda _: self.bindKeys_dummyMode())

    def bindKeys_dummyMode(self) -> None:
        self.gridWindow.bind("c", lambda _: self.handleClickDummyMode())
        # self.gridWindow.bind("<Return>", lambda _: self.mouseEventsCreator.moveMouseToGridActiveRectangleCenter())
        self.gridWindow.bind("<Return>", lambda _: self.handleReturnKey())
        self.gridWindow.bind("v", lambda _: self._changeColor())
        self.gridWindow.bind("h", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentColumn_left))
        self.gridWindow.bind("<Left>", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentColumn_left))
        self.gridWindow.bind("j", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentRow_down))
        self.gridWindow.bind("<Down>", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentRow_down))
        self.gridWindow.bind("k", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentRow_up))
        self.gridWindow.bind("<Up>", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentRow_up))
        self.gridWindow.bind("l", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentColumn_right))
        self.gridWindow.bind("<Right>", lambda _: self.callRectangleMovement(self.activeRectangleKeeper.currentColumn_right))

    def callRectangleMovement(self, movement: Callable) -> None:
        print("movement called!")
        movement()
        self.linesPainter.drawLines()

    def _changeColor(self):
        print("// called _changeColor()")
        self.colorPicker.changeColor()
        self.linesPainter.drawLines()

    def _moreSquares(self):
        print("// do more squares!")
        self.coordsStore.incGridDensity()
        self.linesPainter.drawLines()

    def _lessSquares(self):
        print("// do less squares.")
        self.coordsStore.decGridDensity()
        self.linesPainter.drawLines()

    def handleClickDummyMode(self):
        self.windowActionsCaller.hideWindow()
        self.mouseEventsCreator.sendClick()
        self.bindKeys_dummyMode()

    def handleReturnKey(self):
        self.mouseEventsCreator.moveMouseToGridActiveRectangleCenter()
        self.gridWindow.bind("h", lambda _: self.mouseEventsCreator.activeCursorPositionKeeper.cursor_moveLeft())
        self.gridWindow.bind("j", lambda _: self.mouseEventsCreator.activeCursorPositionKeeper.cursor_moveDown())
        self.gridWindow.bind("k", lambda _: self.mouseEventsCreator.activeCursorPositionKeeper.cursor_moveUp())
        self.gridWindow.bind("l", lambda _: self.mouseEventsCreator.activeCursorPositionKeeper.cursor_moveRight())
        # self.gridWindow.bind("l", lambda _: self.mouseEventsCreator.activeCursorPositionKeeper.)
