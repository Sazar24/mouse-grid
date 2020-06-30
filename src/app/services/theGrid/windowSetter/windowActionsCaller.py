
import tkinter as tk
from injector import inject
# from app.ioc.container.container import AppContainer
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper


class WindowActionsCaller:
    @inject
    # def __init__(self, gridMaker: GridMaker):
    def __init__(self, windowInstanceKeeper: WindowInstanceKeeper):
        self.window: tk.Tk = windowInstanceKeeper.getWindow()

    def bringWindowToTop(self) -> None:
        self.window.update()
        self.window.deiconify()
        self.window.attributes("-topmost", 100)

    def hideWindow(self) -> None:
        print("hideWindow has been called")
        self.window.update()
        self.window.withdraw()
        pass
