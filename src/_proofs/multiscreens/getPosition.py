import tkinter as tk
root = tk.Tk()


def click():
    print(root.winfo_x(), root.winfo_y())


tk.Button(text="Get position", command=click).grid()
root.mainloop()
