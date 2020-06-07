
import tkinter as tk


class WindowActionsCaller:
    # def __init__(self, gridMaker: GridMaker):
    def __init__(self, gridWindow: tk.Tk):
        self.window: tk.Tk = gridWindow

    def bringWindowToTop(self) -> None:
        self.window.update()
        self.window.deiconify()
        self.window.attributes("-topmost", 100)

    def hideWindow(self) -> None:
        print("hideWindow has been called")
        self.window.update()
        self.window.withdraw()
        pass
