import tkinter as tk
from injector import singleton, inject


@singleton
class WindowInstanceKeeper:
    def __init__(self):
        self.tkWindow = tk.Tk()
        # pass

    def getWindow(self) -> tk.Tk:
        return self.tkWindow
