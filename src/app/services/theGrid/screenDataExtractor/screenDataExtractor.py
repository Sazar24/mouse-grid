import tkinter as tk
from injector import inject


class ScreenDataExtractor:
    @inject
    def __init__(self):
        pass

    def getMaxXY(self):
        """ zwraca x, y """
        x, y = self.__getFullScreenSize()
        return x, y

    def __getFullScreenSize(self):
        tempRoot = tk.Tk()
        screen_width = tempRoot.winfo_screenwidth()
        screen_height = tempRoot.winfo_screenheight()
        print(f'screen_width: {screen_width} | screen_height: {screen_height}')
        tempRoot.destroy()
        return screen_width, screen_height
