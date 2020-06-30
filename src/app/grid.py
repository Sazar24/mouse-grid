import tkinter as tk
from injector import singleton, inject

from app.services.theGrid.painter.gridLinesPainter import GridLinesPainter
from app.services.theGrid.keysBinder.keysBinder import KeysBinder
from app.services.theGrid.windowSetter.windowParamSetter import WindowParamSetter
from app.services.globalKeystrokeListerner.globalKeystrokeListerner import GlobalKeystrokeListerner
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper
from app.ioc.container.container import AppContainer


class GridMaker:
    @inject
    def __init__(
            self,
            windowKeeper: WindowInstanceKeeper,
            gridLinesPainter: GridLinesPainter,
            keysBinder: KeysBinder,
            globalKeystrokeListerner: GlobalKeystrokeListerner
    ):
        self.window = windowKeeper.getWindow()
        self.globalKeyslistener = globalKeystrokeListerner
        self.linesPainter = gridLinesPainter
        self.keysBinder: KeysBinder = keysBinder

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
        self.globalKeyslistener.run()

    def _startTkWindowLoop(self) -> None:
        self.window.mainloop()

    def _bindKeys(self) -> None:
        self.keysBinder.bindKeys_dummyMode()
