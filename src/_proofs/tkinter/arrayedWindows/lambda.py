import tkinter as tk


class MasterWindow:
    def __init__(self):
        self.root = tk.Tk()


class ChildWindow:
    def __init__(self, parent):
        self.tkWindow = tk.Toplevel(parent)
