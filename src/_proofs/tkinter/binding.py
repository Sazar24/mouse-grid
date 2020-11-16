import tkinter as tk


def pressed(value: str):
    print(f"key pressed! value: {value}")


root = tk.Tk()
label = tk.Label(width=30)
label.pack(side="top", fill="both", expand=True)

root.bind(1, lambda _: pressed("numeric"))
root.bind("1", lambda _: pressed("str"))
root.bind("a", lambda _: pressed("a"))

root.mainloop()
