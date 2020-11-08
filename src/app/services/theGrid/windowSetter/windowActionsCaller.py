
import tkinter as tk
from injector import inject
# from app.ioc.container.container import AppContainer
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper
from time import sleep


class WindowActionsCaller:
    @inject
    # def __init__(self, gridMaker: GridMaker):
    def __init__(self, windowInstanceKeeper: WindowInstanceKeeper):
        self.window: tk.Tk = windowInstanceKeeper.getWindow()

    def bringWindowToTop(self) -> None:
        self.window.update()
        self.window.deiconify()

        self.window.focus_set()
        # self.window.wm_deiconify()
        # self.window.protocol("WM_DELETE_WINDOW", self.window.iconify)
        self.window.attributes("-topmost", 100)
        # self.window.attributes('-topmost', True)
        # self.window.attributes('-topmost', False)
        # self.window.lift()
        # sleep(0.001)
        print("hideWindow has been called")
        self.window.overrideredirect(True)
        self.window.after(1, lambda: self.window.focus_force())

    def __ifAlreadyVisibleShowOnTaskbar(self):
        # TODO
        """
        Kiedy aplikacja jest widoczna, ale użytkownik przełączy się na inną (clickiem lub alt+tab),
        okno MouseGrida traci focus i ciężko jest go przywrócić.
        (W tym celu najprawdopodniej trzeba będzie przywrócić aplikacji ikonę na taskbarze i bawić się w jej odnajdywanie
        i focusowanie)
        """
        pass

    def hideWindow(self) -> None:
        print("hideWindow has been called")
        self.window.overrideredirect(False)
        self.window.update()
        self.window.withdraw()

    def terminateProgram(self) -> None:
        self.window.destroy()
