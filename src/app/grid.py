import tkinter as tk

from src.app.services.theGrid.painter.gridLinesPainter import GridLinesPainter
from src.app.services.theGrid.keysBinder.keysBinder import KeysBinder
from src.app.services.theGrid.windowSetter.windowParamSetter import WindowParamSetter
from src.app.services.globalKeystrokeListerner.globalKeystrokeListerner import GlobalKeystrokeListerner


class GridMaker:
    def __init__(self):
        self.window = tk.Tk()
        self.__listener = GlobalKeystrokeListerner(self.window)
        self.linesPainter = GridLinesPainter()
        self.keysBinder = KeysBinder(self.linesPainter, self.window)

    def run(self) -> None:
        print("Starting grid...")
        self.initiateAndStartWindow()

    def initiateAndStartWindow(self) -> None:
        self._startListening()
        self._setWindowParams()
        self._drawLines()
        self._bindKeys()
        self._startTkWindowLoop()

    def _setWindowParams(self) -> None:
        WindowParamSetter().setParams(self.window)

    def _drawLines(self) -> None:
        self.linesPainter.drawLines()

    def _startListening(self) -> None:
        self.__listener.run()

    def _startTkWindowLoop(self) -> None:
        self.window.mainloop()

    def _bindKeys(self) -> None:
        self.keysBinder.bindKeys_dummyMode()
