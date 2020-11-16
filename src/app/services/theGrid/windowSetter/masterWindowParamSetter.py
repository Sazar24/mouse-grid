import tkinter as tk
from injector import inject
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper


class MasterWindowParamSetter:
    @inject
    def __init__(self, windowInstanceKeeper: masterWindowInstanceKeeper):
        self.windowInstanceKeeper = windowInstanceKeeper

    def setParams(self) -> None:
        self.tkWindowObject = self.windowInstanceKeeper.getWindow()
        self.tkWindowObject.geometry("700x700+100+100")

        # self._makeWindowTransparent()
        # self._makeWindowFullscreen()
        self._setAppTitle()
        self.__hideTopWindow()
        # self.__hideWindowFromTaskbar()
        # self.__makeMultiScreen()
        # self.__decor()

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
        # self.tkWindowObject.overrideredirect(True)
        self.tkWindowObject.update()
        self.tkWindowObject.withdraw()

    def __makeMultiScreen(self):
        """ Na razie eksperymentalnie tylko """
        self.tkWindowObject.geometry("1920x1080-1900-0")

    def __decor(self):
        self.tkWindowObject.geometry("700x700+100+100")
        label = tk.Label(self.tkWindowObject, text="masterWindow")
        label.place(x=-21, y=33)

    def __hideTopWindow(self):
        self.tkWindowObject.withdraw()
        # self.tkWindowObject.withdraw()
