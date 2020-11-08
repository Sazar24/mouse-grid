import tkinter as tk
from injector import singleton, inject

from app.services.theGrid.painter.gridLinesPainter import GridLinesPainter
from app.services.theGrid.keysBinder.keysBinder import KeysBinder
from app.services.theGrid.windowSetter.windowParamSetter import WindowParamSetter
from app.services.globalKeystrokeListerner.globalKeystrokeListerner import GlobalKeystrokeListerner
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper
from app.modes.focuser.focuserMode import Focuser
# from app.ioc.container.container import AppContainer
from time import sleep

# transparency / alpha:
# https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent/54645103


class App:
    @inject
    def __init__(
            self,
            windowKeeper: WindowInstanceKeeper,
            gridLinesPainter: GridLinesPainter,
            keysBinder: KeysBinder,
            globalKeystrokeListerner: GlobalKeystrokeListerner,
            windowParamSetter: WindowParamSetter,
            zoomer: Focuser
    ):
        self.window = windowKeeper.getWindow()
        self.globalKeyslistener = globalKeystrokeListerner
        self.linesPainter = gridLinesPainter
        self.keysBinder: KeysBinder = keysBinder
        self.windowParamSetter: WindowParamSetter = windowParamSetter
        self.zoomer = zoomer

    def run(self) -> None:
        print("Starting grid...")
        self.__initiateAndStartWindow()

    def __initiateAndStartWindow(self) -> None:
        self._startListening()
        self._setWindowParams()
        self._drawLines()
        # self._bindKeys()
        self._startTkWindowLoop()

    def _setWindowParams(self) -> None:
        self.windowParamSetter.setParams()

    def _drawLines(self) -> None:
        # self.linesPainter.drawLines()
        self.zoomer.showMe()

    def _startListening(self) -> None:
        self.globalKeyslistener.run()

    def _startTkWindowLoop(self) -> None:
        # self.window.geometry("1920x1080-1680-0")
        # self.window.wm_attributes('-fullscreen', 'true')
        # self.window.overrideredirect(True)
        # self.window.geometry("1920x1080-1680-0")
        # self.window.attributes('-topmost', True)
        # self.window.update()
        self.window.mainloop()

    def _bindKeys(self) -> None:
        self.keysBinder.bindKeys_dummyMode()
