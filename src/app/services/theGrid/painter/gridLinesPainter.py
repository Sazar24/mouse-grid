import tkinter as tk
from typing import Tuple, List
from injector import singleton, inject
from app.services.theGrid.screenDataExtractor.screenDataExtractor import ScreenDataExtractor
from app.services.theGrid.gridInfoStore.gridLinesCoordsStore import GridLinesCoordsStore
from app.services.theGrid.gridInfoStore.gridColorKeeper import GridColorKeeper
from app.services.theGrid.gridInfoStore.activeRectangleKeeper import ActiveRectangleKeeper
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper


@singleton
class GridLinesPainter():
    @inject
    def __init__(self, windowInstanceKeeper: masterWindowInstanceKeeper):
        self.gridWindow: tk.Tk = windowInstanceKeeper.getWindow()
        self.gridDensity: int = 15
        self.__initFullscreenCanvas()
        self.coordsStore = GridLinesCoordsStore()
        self.colorPicker = GridColorKeeper()
        # self.color = "gray15"
        self.color = self.colorPicker.getActiveColor()
        self.activeRectangleKeeper = ActiveRectangleKeeper()

    def __initFullscreenCanvas(self) -> None:
        self.maxX, self.maxY = ScreenDataExtractor().getMaxXY()
        options = {
            "width": self.maxX,
            "height": self.maxY,
            # "background": "green",
            "highlightthickness": 0
        }
        self.gridCanvas = tk.Canvas(self.gridWindow, **options)

    def drawLines(self) -> None:
        # self.__drawGridAsLines()
        self.__drawMultiFrames()

    # #### drawing lines:

    def __drawGridAsLines(self):
        self.color = self.colorPicker.getActiveColor()
        self.gridCanvas.delete('all')
        self.coordsStore.calculateAllLinesCoordinates()
        self.__drawColumns()
        self.__drawRows()
        self._drawActiveRectangle()
        self.gridCanvas.pack()

    # def drawRectangle(self):
    #     self.gridCanvas.create_line(12, 12, 566, 666, fill="blue")
    #     self.gridCanvas.pack()

    def _drawActiveRectangle(self):
        self.__drawBoldOutlineOnActiveRectangle(8)

    def __drawColumns(self):
        verticalLines: Tuple[int, int, int, int] = self.coordsStore.getAllVertcicalLines()
        for lineCoords in verticalLines:
            self.gridCanvas.create_line(lineCoords, fill=self.color)

    def __drawRows(self):
        horizontalLines: Tuple[int, int, int, int] = self.coordsStore.getAllHorizontalLines()
        for lineCoords in horizontalLines:
            self.gridCanvas.create_line(lineCoords, fill=self.color)

    def __drawBoldOutlineOnActiveRectangle(self, boldValue: int) -> None:
        rectanglePoints: List[Tuple[int, int]] = self.activeRectangleKeeper.getActiveRectangleCoords()
        rectangleCornerPoint_topLeft: Tuple[int, int] = rectanglePoints[0]
        rectangleCornerPont_topRight: Tuple[int, int] = rectanglePoints[1]
        rectangleCornerPoint_bottomRight: Tuple[int, int] = rectanglePoints[2]
        rectangleCornerPoint_bottomLeft: Tuple[int, int] = rectanglePoints[3]

        for px in range(1, boldValue):
            self.gridCanvas.create_line(
                rectangleCornerPoint_topLeft[0] - px,
                rectangleCornerPoint_topLeft[1] - px,
                rectangleCornerPont_topRight[0] + px,
                rectangleCornerPont_topRight[1] - px,
                fill="green"
            )
            self.gridCanvas.create_line(
                rectangleCornerPont_topRight[0] + px,
                rectangleCornerPont_topRight[1] - px,
                rectangleCornerPoint_bottomRight[0] + px,
                rectangleCornerPoint_bottomRight[1] + px,
                fill="yellow"
            )
            self.gridCanvas.create_line(
                rectangleCornerPoint_bottomRight[0] + px,
                rectangleCornerPoint_bottomRight[1] + px,
                rectangleCornerPoint_bottomLeft[0] - px,
                rectangleCornerPoint_bottomLeft[1] + px,
                fill="red"
            )
            self.gridCanvas.create_line(
                rectangleCornerPoint_bottomLeft[0] - px,
                rectangleCornerPoint_bottomLeft[1] + px,
                rectangleCornerPoint_topLeft[0] - px,
                rectangleCornerPoint_topLeft[1] - px,
                fill="white"
            )

    # #### end of drawing grid as lines

    def __drawMultiFrames(self):
        # self.gridCanvas.delete('all')
        # self.gridCanvas.create_line(lineCoords, fill=self.color)
        # frame = tk.Frame(self.gridWindow, bd='2')
        # nameentryframe = Frame(master, background='BLACK', borderwidth=14, relief=SUNKEN)
        # frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        # frame.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5)
        frameParams = {
            'borderwidth': 1,
            'background': 'red',
            'highlightbackground': 'white',
            'width': 50,
            'height': 50
        }
        # for i in range(10):
        # frame = tk.Frame(self.gridWindow, borderwidth=1, background='gray')
        # frame.grid(row=i, column=i, sticky="nsew")
        # frame1 = tk.Frame(self.gridWindow, **frameParams)
        # frame2 = tk.Frame(self.gridWindow, **frameParams)
        # frame1.grid(row=0, column=0)
        # frame2.grid(row=1, column=1)
        frame1 = tk.Frame(self.gridWindow, bg='green', highlightbackground='green', borderwidth=16)
        canvas1 = tk.Canvas(frame1)
        # canvas1.place()

        frame2 = tk.Frame(self.gridWindow, bg='blue', highlightbackground='blue', borderwidth=5)
        canvas2 = tk.Canvas(frame2)
        canvas2.pack()

        frame3 = tk.Frame(self.gridWindow, bg='yellow', highlightbackground='yellow', borderwidth=5)
        canvas3 = tk.Canvas(frame2)
        canvas3.pack()
        # frame2.configure
        frame1.grid(column=0, row=0)
        frame2.grid(column=1, row=1)
        frame3.grid(column=2, row=2)
        print(frame1.size)

        # frame2.configure(command=lambda: frame2.tkraise())
        # frame.place(relwidth=1, relheight=1)
        # frame.place()
        # button = tk.Button(frame1, text='ccc', bg='yellow', fg='red')
        # button.pack()
        # button2 = tk.Button(frame3, text='', bg='yellow', fg='red')
        # button2.pack()
        # button2 = tk.Button(frame2, text='ccc', bg='yellow', fg='red')
        # button2.pack()
        # self.gridCanvas.pack()
