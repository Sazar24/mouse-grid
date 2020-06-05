# from ...interfaces.runnable import IRunnable  # type: ignore
# from interface import implements
from ..globalKeystrokeListerner.globalKeystrokeListerner import GlobalKeystrokeListerner
import tkinter as tk

# class GridMaker(implements(IRunnable)):


class GridMaker:
    def __init__(self):
        self.__listener__ = GlobalKeystrokeListerner()
        self.window = tk.Tk()
        pass

    def run(self) -> None:
        print("Starting grid...")
        self.initiateAndStartWindow()
        pass

    def initiateAndStartWindow(self) -> None:
        self._startListening()
        self._drawLines()
        self.bindKeys()
        self.startTkWindowLoop()
        self._startCalc()

    def bringWindowToTop(self) -> None:
        self.window.update()
        self.window.deiconify()
        pass

    def hideWindow(self) -> None:
        self.window.update()
        self.window.withdraw()
        pass

    def _drawLines(self) -> None:
        pass

    def _startListening(self) -> None:
        self.__listener__.callOn_i_ = self._sthCallable
        self.__listener__.passActionCallers(
            self.hideWindow,
            self.bringWindowToTop
        )
        self.__listener__.run()

    def _sthCallable(self) -> None:
        print("I have been called")
        self.innerNr += 100

    innerNr: int = 0

    def _startCalc(self) -> None:
        from time import sleep
        for i in range(0, 7):
            self.innerNr += 1
            print(f"{i}: {self.innerNr}")
            sleep(1)
            pass

    def startTkWindowLoop(self) -> None:
        self.window.mainloop()

    def bindKeys(self) -> None:
        self.window.bind("k", lambda _: print("k pressed"))
