# https://stackoverflow.com/questions/26286660/how-to-make-a-window-fullscreen-in-a-secondary-display-with-tkinter
import tkinter as tk


class FullScreen2:
    def __init__(self):
        self.tkWindow = tk.Tk()

    def run(self):
        bothWidth: int = 1920
        height: int = 1080
        # self.tkWindow.geometry(f"{bothWidth}x1080-400+0")
        # self.tkWindow.geometry(f"{bothWidth}x{height}-1680+0")
        # self.tkWindow.geometry("-1489+0")
        # self.tkWindow.geometry("-1490+0")
        # self.tkWindow.geometry("-2490-19")
        self.tkWindow.geometry("4x4-1900-0")
        # self.tkWindow.overrideredirect(True)s
        self.tkWindow.state("zoomed")
        # canvas: tk.Canvas = tk.Canvas(self.tkWindow)
        # canvas.create_line(2, 2, bothWidth - 100, height, fill='red')
        # canvas.pack()
        # print(self.tkWindow.winfo_x(), self.tkWindow.winfo_y())
        tk.Button(text="Get position", command=self.click).grid()
        self.tkWindow.wm_title("hi")
        # self.tkWindow.mainloop()
        # self.tkWindow.after(0, self.click())

    def click(self):
        print(self.tkWindow.winfo_x(), self.tkWindow.winfo_y())


app = FullScreen2()

app.run()
app.click()
# print("hej?")

app.tkWindow.mainloop()
# app.tkWindow.after(0, self.click())
