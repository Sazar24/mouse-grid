import tkinter as tk
from injector import inject
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper


class WindowParamSetter:
    @inject
    def __init__(self, windowInstanceKeeper: masterWindowInstanceKeeper):
        self.windowInstanceKeeper = windowInstanceKeeper

    def setParams(self) -> None:
        self.tkWindowObject = self.windowInstanceKeeper.getWindow()

        # self._makeWindowTransparent()
        # self._makeWindowFullscreen()
        self._setAppTitle()
        # self.__hideWindowFromTaskbar()
        # self.__makeMultiScreen()

    def _makeWindowFullscreen(self) -> None:
        self.tkWindowObject.wm_attributes('-fullscreen', 'true')
        # self.tkWindowObject.state("zoomed")

    def _makeWindowTransparent(self) -> None:
        self.tkWindowObject.attributes('-transparentcolor', self.tkWindowObject['bg'])

    def _setAppTitle(self) -> None:
        self.tkWindowObject.title("mouse-grid")

    def __hideWindowFromTaskbar(self):
        """
        source: https://stackoverflow.com/questions/59437366/python-tkinter-how-to-disable-window-showing-in-taskbar
        Niby działa, ale tracę focusa na aplikacji i okno jako takie nie istnieje - nie można się na nim sfocusować.
        """
        self.tkWindowObject.overrideredirect(True)

    def __makeMultiScreen(self):
        """ Na razie eksperymentalnie tylko """
        self.tkWindowObject.geometry("1920x1080-1900-0")
