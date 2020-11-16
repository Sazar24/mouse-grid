
from injector import inject
from time import sleep
import tkinter as tk
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper
from app.services.handlingMultiScreen.storages.WindowsStore import WindowsStore
from app.services.handlingMultiScreen.screenWindow import ScreenWindow


class WindowActionsCaller:
    @inject
    # def __init__(self, gridMaker: GridMaker):
    def __init__(self,
                 masterWindowInstanceKeeper: masterWindowInstanceKeeper,
                 windowsStore: WindowsStore,
                 ):
        self.masterWindow: tk.Tk = masterWindowInstanceKeeper.getWindow()
        self.windowsStore: WindowsStore = windowsStore

    def bringAppToTop(self) -> None:
        """
        KnownIssues:
        #1: gdy aplikacja aktywna, alt+tab buguje niniejszą funkcję
        #2: Naprzemienne ukrywanie apki i przywoływanie jej, przesuwa oknoNr2

        #1. Użyj pynputa
        """

        allWindows = self.windowsStore.getWindows()
        for knownMonitor in allWindows:
            knownMonitor.windowForScreen.update()
            knownMonitor.windowForScreen.deiconify()
        # allWindows[1].windowForScreen.update()

        # self.masterWindow.overrideredirect(False)
        # self.masterWindow.update()

        # self.masterWindow.deiconify()
        # self.masterWindow.focus_set()
        # self.masterWindow.focus_force()

        # self.masterWindow.attributes("-topmost", 100)
        # self.masterWindow.overrideredirect(True)
        # self.masterWindow.after(1, lambda: self.masterWindow.focus_force())
        # self.masterWindow.focus_force()
        # current = self.masterWindow.focus_get()
        # print(current)
        # allWindows[1].windowForScreen.overrideredirect(False)
        # allWindows[1].windowForScreen.overrideredirect(False)
        # allWindows[1].windowForScreen.attributes('-topmost', True)
        # # allWindows[1].windowForScreen.attributes('-topmost', False)
        allWindows[1].windowForScreen.focus_set()
        allWindows[1].windowForScreen.focus_force()
        # # allWindows[1].windowForScreen.focus_set()
        # allWindows[1].windowForScreen.after(1, lambda _: allWindows[1].windowForScreen.focus_force())
        # allWindows[1].windowForScreen.after(1, allWindows[1].windowForScreen.focus_force())
        # allWindows[1].windowForScreen.overrideredirect(True)
        # allWindows[1].windowForScreen.update()

    def bringWindowToTop(self, numericId: int):
        for knownMonitor in self.windowsStore.getWindows():
            if knownMonitor.id == numericId:
                knownMonitor.windowForScreen.update()
                # knownMonitor.windowForScreen.focus_force()
                # knownMonitor.windowForScreen.attributes("-topmost", 100)
                # knownMonitor.windowForScreen.focus_set()
                knownMonitor.windowForScreen.deiconify()
                # knownMonitor.windowForScreen.attributes("-topmost", 100)
                knownMonitor.windowForScreen.focus_force()
                knownMonitor.windowForScreen.update()

    def __ifAlreadyVisibleShowOnTaskbar(self):
        # TODO
        """
        Kiedy aplikacja jest widoczna, ale użytkownik przełączy się na inną (clickiem lub alt+tab),
        okno MouseGrida traci focus i ciężko jest go przywrócić.
        (W tym celu najprawdopodniej trzeba będzie przywrócić aplikacji ikonę na taskbarze i bawić się w jej odnajdywanie
        i focusowanie)
        """
        pass

    # def hideWindowsExceptGivenOne(self, window: ScreenWindow):
    # def hideWindowsExceptGivenOne(self, numericId: int):
    def hideWindowsExceptGivenOne(self, _id: int):
        # print(f"Attempt to hide all except window with numericId: {window.numericId} and name: {window._id}.")
        print(f"Attempt to hide all except window with id: {_id}")
        for knownMonitor in self.windowsStore.getWindows():
            if knownMonitor.id != _id:
                print(f"Hiding window with id: {knownMonitor.id}, name: {knownMonitor.name}. (visible-screeenId: {_id})")
                self._hideWindow(knownMonitor)
        self.bringWindowToTop(_id)

    def _hideWindow(self, window: ScreenWindow):
        # window.windowForScreen.overrideredirect(False)
        # window.windowForScreen.update()
        window.windowForScreen.withdraw()
        # window.windowForScreen.destroy()

    def hideApp(self) -> None:
        print("hideApp has been called")
        # self.masterWindow.overridideredirect(False)
        # self.masterWindow.update()
        self.masterWindow.withdraw()
        for knownWindow in self.windowsStore.getWindows():
            knownWindow.windowForScreen.withdraw()

    def terminateProgram(self) -> None:
        self.masterWindow.destroy()
