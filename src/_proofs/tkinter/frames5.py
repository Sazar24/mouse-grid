import tkinter as tk


class Proof:
    def __init__(self):
        pass

    def run(self):
        self.doDrawing()
        self.window.mainloop()

    def doDrawing(self):
        self.window: tk.Tk = tk.Tk()
        length = 70
        # tk.mainFrame = tk.Frame(self.window, width=length, bg='blue')
        # mainFrame = tk.Frame(self.window, width=length, bg='yellow')
        # canvas1 = tk.Canvas(self.window, bg='red')

        self.window.geometry(f"{length * 12}x{length * 5}")
        frames = []
        colors = ['red', 'blue', 'white',
                  'green', 'aqua', "red", "cyan",
                  "lightPink1", "lightBlue", "rosy brown", "green", "deepPink2", '#a99e9e',
                  '#b757a0', '#5e4fbf', '#281d71',
                  '#1d716b', '#1d712d', "#86a00f",
                  "#a94e1d", "#d87a0a"
                  ]
        colorsAmount = len(colors)

        nthColor = 0

        for y in range(1, 5):
            for x in range(1, 5):
                frame = tk.Frame(self.window, width=length, height=length, bg=colors[nthColor])
                # frame.pack(side='left')
                # frame.place(x=x * length, y=y * length)
                frame.place(x=x * length, y=y * length)
                nthColor += 1
                print(colors[nthColor])
                print(nthColor)

        # mainFrame.grid()
        # frame2.place()
        # frame3.pack()


if __name__ == "__main__":
    app = Proof()
    app.run()
