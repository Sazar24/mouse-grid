import tkinter as tk
from time import sleep
from injector import singleton, inject

from app.services.theGrid.painter.gridLinesPainter import GridLinesPainter
# from app.services.theGrid.keysBinder.keysBinder import KeysBinder
from app.services.theGrid.windowSetter.masterWindowParamSetter import MasterWindowParamSetter
from app.services.globalKeystrokeListerner.globalKeystrokeListerner import GlobalKeystrokeListerner
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper
from app.modes.focuser.focuserMode import Focuser
from app.services.handlingMultiScreen.windowsMaker import WindowsMaker
# from app.ioc.container.container import AppContainer

# transparency / alpha:
# https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent/54645103


class App:
    @inject
    def __init__(
            self,
            windowKeeper: masterWindowInstanceKeeper,
            gridLinesPainter: GridLinesPainter,
            # keysBinder: KeysBinder,
            globalKeystrokeListener: GlobalKeystrokeListerner,
            windowParamSetter: MasterWindowParamSetter,
            focuser: Focuser,
            windowsMaker: WindowsMaker
    ):
        self.window = windowKeeper.getWindow()
        self.globalKeysListener = globalKeystrokeListener
        self.linesPainter = gridLinesPainter
        # self.keysBinder: KeysBinder = keysBinder
        self.windowParamSetter: MasterWindowParamSetter = windowParamSetter
        self.focuser = focuser
        self.windowsMaker = windowsMaker

    def run(self) -> None:
        print("Starting grid...")
        self.__initiateAndStartWindow()

    def __initiateAndStartWindow(self) -> None:
        self._startListening()
        self.__prepareWindows()
        self.__setWindowParams()
        self._drawLines()
        # self._bindKeys()
        self._startTkWindowLoop()

    def __setWindowParams(self) -> None:
        self.windowParamSetter.setParams()

    def _drawLines(self) -> None:
        # self.linesPainter.drawLines()
        self.focuser.showMe()

    def _startListening(self) -> None:
        self.globalKeysListener.run()

    def _startTkWindowLoop(self) -> None:
        # self.window.geometry("1920x1080-1680-0")
        # self.window.wm_attributes('-fullscreen', 'true')
        # self.window.overrideredirect(True)
        # self.window.geometry("1920x1080-1680-0")
        # self.window.attributes('-topmost', True)
        # self.window.update()
        self.window.mainloop()

    # def _bindKeys(self) -> None:
    #     self.keysBinder.bindKeys_dummyMode()

    def __prepareWindows(self) -> None:
        self.windowsMaker.run()
