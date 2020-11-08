# https://stackoverflow.com/questions/26286660/how-to-make-a-window-fullscreen-in-a-secondary-display-with-tkinter
import tkinter as tk


class FullScreen2:
    def __init__(self):
        self.tkWindow = tk.Tk()

    def run(self):
        bothWidth: int = 1920
        height: int = 1080
        # self.tkWindow.geometry(f"{bothWidth}x1080-400+0")
        self.tkWindow.geometry(f"{bothWidth}x{height}-1680+0")
        self.tkWindow.overrideredirect(True)
        self.tkWindow.state("zoomed")
        canvas: tk.Canvas = tk.Canvas(self.tkWindow)
        canvas.create_line(2, 2, bothWidth - 100, height, fill='red')
        canvas.pack()
        print(self.tkWindow.winfo_x(), self.tkWindow.winfo_y())
        self.tkWindow.wm_title("hi")
        self.tkWindow.mainloop()


FullScreen2().run()