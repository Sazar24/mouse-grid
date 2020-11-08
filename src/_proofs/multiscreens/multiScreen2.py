import tkinter as tk


class MultiScreenWindow:
    def __init__(self):
        self.tkWindow = tk.Tk()

    def run(self):
        bothWidth: int = 1920 + 1680
        height: int = 1080
        # self.tkWindow.geometry(f"{bothWidth}x1080-400+0")
        self.tkWindow.geometry(f"{bothWidth}x{height}-1+0")
        currGeo = self.tkWindow.geometry()
        print(currGeo)
        canvas: tk.Canvas = tk.Canvas(self.tkWindow)
        canvas.create_line(2, 2, bothWidth - 100, height, fill='red')
        canvas.pack()
        print(self.tkWindow.winfo_x(), self.tkWindow.winfo_y())
        self.tkWindow.wm_title("hi")
        self.tkWindow.mainloop()


MultiScreenWindow().run()
