# https://stackoverflow.com/questions/32467085/tkinter-why-the-perimeter-of-a-rectangle-grid-is-not-showing
import tkinter as tk


class GridWindow:
    def __init__(self, parent: tk.Tk):
        self.myParent = parent

        self.myContainer1 = tk.Frame(parent)
        self.myContainer1.pack()
        self.masterContainer = tk.Frame(parent, width=500, height=500)
        self.masterContainer.pack()

        self.cellwidth = 25
        self.cellheight = 25

    def draw_grid(self, rows, columns):
        myCanvas = tk.Canvas(self.myContainer1, width=self.cellheight * rows,
                             height=self.cellwidth * columns)
        myCanvas.pack()

        for column in range(rows):
            for row in range(columns):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                myCanvas.create_rectangle(x1, y1, x2, y2, fill="")

    def drawGridWithFrames(self, rows, columns):
        tileFrame = tk.Frame(self.masterContainer, width=400, height=460,)
        for column in range(rows):
            # for row in range(columns):
            tileCanvas = tk.Canvas(tileFrame, width=30, height=30)
            tileCanvas.create_rectangle(0, 0, 80, 99, fill="red")
            tileCanvas.pack(side='left', fill='both')
        tileFrame.pack()


def runApp(rows, columns):
    root = tk.Tk()
    myapp = GridWindow(root)
    # myapp.drawGridWithFrames(rows, columns)
    myapp.draw_grid(5, 5)
    root.mainloop()


if __name__ == '__main__':
    runApp(10, 10)
