import tkinter as tk
from screeninfo.common import Monitor


class ScreenWindow:
    amIFocused: bool = False

    def __init__(self, parentWindow: tk.Tk, monitor: Monitor, _id: int):
        self.parentWindow = parentWindow
        self.monitor = monitor
        self.name = self.__clearName(monitor.name)
        self.id: int = _id
        self.__createMe(monitor)
        # self.frame = tk.Frame(self.master)
        # self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        # self.quitButton.pack()
        # self.frame.pack()
        self.lastText = self.canvas.create_text(0, 60, text=".", fill="red", anchor=tk.NW)

    def __createMe(self, monitor: Monitor):
        self.windowForScreen = tk.Toplevel(self.parentWindow)
        self.windowForScreen.title(monitor.name)
        self.__setPosition(monitor)
        self.__hideWindowFromTaskbar()
        self.__makeFullScreen()
        self.__makeTransparent()
        self.addFullScreenCanvas()
        self.showName()
        # self.hideName()
        print(f"Window '{self.name}' has been created.")

    def close_windows(self):
        self.master.destroy()

    def __setPosition(self, monitorData: Monitor):
        """
        TODO: Tutaj chyba jest błąd. Przy określaniu window.geometry powinienem
              uwzględnić szerokość/wysokość głównego ekranu.
              Poniżej wersja robocza
        """
        # x: int = 0
        # if monitorData.x < 0:
        #     x = -1680
        x = monitorData.x
        y = monitorData.y
        self.windowForScreen.geometry(f"500x500+{x}+{y}")
        # self.windowForScreen.geometry("0x0")

    def __calcScreenPosition(self, monitorData: Monitor):
        pass

    def __makeFullScreen(self):
        self.windowForScreen.state("zoomed")
        self.windowForScreen.overrideredirect(True)

    def __hideWindowFromTaskbar(self):
        self.windowForScreen.overrideredirect(True)

    def __makeTransparent(self) -> None:
        self.windowForScreen.attributes('-transparentcolor', self.windowForScreen['bg'])

    def __clearName(self, txt: str) -> str:
        result = ""
        for char in txt:
            if char.isnumeric() or char.isalpha():
                result += char

        if len(result) == 0:
            result = txt

        return result

    def addFullScreenCanvas(self):
        width = self.monitor.width
        height = self.monitor.height
        self.canvas = tk.Canvas(self.windowForScreen, width=width, height=height,
                                bd=0, highlightthickness=0)
        self.canvas.pack()

    def showName(self):
        x = 0
        y = 0
        self.textBg = self.canvas.create_rectangle(x, y, 125, 90, fill="gray", outline=None)
        self.name_textId = self.canvas.create_text(x, y, text=f"id: {self.name}", fill="green", anchor=tk.NW)
        self.canvas.create_text(x, y + 23, text=f"id: {self.id}", fill="green", anchor=tk.NW)

    def showText(self, txt):
        self.canvas.delete(self.lastText)
        self.lastText = self.canvas.create_text(0, 60, text=f"{txt}", fill="red", anchor=tk.NW)

    def hideName(self):
        self.canvas.delete(self.textBg)
        self.canvas.delete(self.name_textId)
