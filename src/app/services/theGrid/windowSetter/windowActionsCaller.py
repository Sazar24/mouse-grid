
from injector import inject
from time import sleep
import tkinter as tk
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper
from app.services.handlingMultiScreen.storages.WindowsStore import WindowsStore
from app.services.handlingMultiScreen.screenWindow import ScreenWindow
from app.services.handlingMultiScreen.activityHandler.focusedScreenKnower import FocusedScreenManager


class WindowActionsCaller:
    @inject
    # def __init__(self, gridMaker: GridMaker):
    def __init__(self,
                 masterWindowInstanceKeeper: masterWindowInstanceKeeper,
                 windowsStore: WindowsStore,
                 focusedScreenManager: FocusedScreenManager
                 ):
        self.masterWindow: tk.Tk = masterWindowInstanceKeeper.getWindow()
        self.windowsStore: WindowsStore = windowsStore
        self.focusedScreenManager: FocusedScreenManager = focusedScreenManager

    def bringAppToTop(self) -> None:
        """
        KnownIssues:
        #1: gdy aplikacja aktywna, alt+tab buguje niniejszą funkcję
        #2: Naprzemienne ukrywanie apki i przywoływanie jej, przesuwa oknoNr2

        solutions:
        #1. Użyj pynputa
        """

        allWindows = self.windowsStore.getWindows()
        for knownMonitor in allWindows:
            knownMonitor.windowForScreen.update()
            knownMonitor.windowForScreen.deiconify()

        sleep(0.001)
        allWindows[0].windowForScreen.focus_set()
        allWindows[0].windowForScreen.focus_force()

    def bringWindowToTop(self, numericId: int):
        for knownMonitor in self.windowsStore.getWindows():
            if knownMonitor.id == numericId:
                print(f"bringing to top window with id: {numericId}")
                # knownMonitor.windowForScreen.update()
                # knownMonitor.windowForScreen.focus_set()
                knownMonitor.windowForScreen.deiconify()
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
        print(f"Attempt to hide all except window with id: {_id}")
        for knownMonitor in self.windowsStore.getWindows():
            if knownMonitor.id != _id:
                print(f"Hiding window with id: {knownMonitor.id}, name: {knownMonitor.name}. (visible-screeenId: {_id})")
                self._hideWindow(knownMonitor)
        self.bringWindowToTop(_id)
        self.focusedScreenManager.ensureScreenWindowFocus(_id)

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
