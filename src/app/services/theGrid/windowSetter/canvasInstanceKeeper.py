import tkinter as tk
from injector import singleton, inject
from app.modes.models.rectangle import Rectangle
from app.services.theGrid.screenDataExtractor.screenDataExtractor import ScreenDataExtractor
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper


@singleton
class CanvasInstanceKeeper:
    @inject
    def __init__(self,
                 windowInstanceKeeper: masterWindowInstanceKeeper,
                 screenDataExtractor: ScreenDataExtractor
                 ):
        self.screenDataExtractor = screenDataExtractor
        self.windowInstanceKeeper: tk.Tk = windowInstanceKeeper
        self.__initiate()

    def __initiate(self):
        tkWindow: tk.Tk = self.windowInstanceKeeper.getWindow()
        maxX, maxY = self.screenDataExtractor.getMaxXY()
        self.maxCell: Rectangle = Rectangle(0, 0, width=maxX, height=maxY)
        self.frame = tk.Frame(tkWindow, width=maxX, height=maxY)
        self.frame.pack()
        self.fullScreenCanvas = tk.Canvas(self.frame, width=maxX, height=maxY)
        self.fullScreenCanvas.pack()

    def getCanvas(self) -> tk.Canvas:
        return self.fullScreenCanvas
