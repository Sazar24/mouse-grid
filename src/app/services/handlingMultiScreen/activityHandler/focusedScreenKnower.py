import tkinter as tk
from injector import inject, singleton
from app.services.handlingMultiScreen.storages.WindowsStore import WindowsStore
from app.services.handlingMultiScreen.screenWindow import ScreenWindow
from app.ioc.container.container import AppContainer
# from app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller


@singleton
class FocusedScreenManager:
    @inject
    def __init__(self,
                 windowsStore: WindowsStore,
                 # windowActionsCaller: WindowActionsCaller
                 ):
        self.windowsStore = windowsStore
        # self.windowActionsCaller = windowActionsCaller
        self.activeScreenNumericId = 0

    # def setScreen_focusedIn(self, screenNumericId: int):
    def setScreen_focusedIn(self, screen: ScreenWindow):
        # self.activeScreenNumericId = screenNumericId
        # for screen in self.windowsStore.getWindows():
        #     screen.
        print(f"Screen focused in: name: {screen.name}")
        screen.amIFocused = True
        screen.showText("focused in.")

    def setScreen_focusedOut(self, screen: ScreenWindow):
        """ window can lost focus in many ways.
        We have to capture outside-this-program events."""
        print(f"screen focused out: name: {screen.name}")
        screen.showText("focused out.")
        screen.amIFocused = False
        self.hideAppWhenLostFocus()

    def ensureScreenWindowFocus(self, screenNumericId: int):
        # TODO
        # propably pynput and app-handle (extracted via PID) will be required.
        pass

    def monitorWindowsFocusState(self):
        windows = self.windowsStore.getWindows()
        for win in windows:
            currentWin = win
            currentWin.windowForScreen.bind("<FocusIn>", self.__getLambdaAction_focusIn(currentWin))
            currentWin.windowForScreen.bind("<FocusOut>", self.__getLambdaAction_focusOut(currentWin))
            # currentWin.windowForScreen.bind("<FocusIn>", lambda _: self.setScreen_focusedIn(win))
            # currentWin.windowForScreen.bind("<FocusOut>", lambda _: self.setScreen_focusedOut(win))

    def __getLambdaAction_focusIn(self, win: ScreenWindow):
        return lambda _: self.setScreen_focusedIn(win)

    def __getLambdaAction_focusOut(self, win: ScreenWindow):
        return lambda _: self.setScreen_focusedOut(win)

    def hideAppWhenLostFocus(self):
        return
        """ TODO. BUGGED, Doesnt work. """
        print("hideAppWhenLostFocus - has been called. ")

        windows = self.windowsStore.getWindows()
        howManyHasNoFocus: int = 0
        for win in windows:
            if win.amIFocused is False:
                howManyHasNoFocus += 1

        print(f"howManyHasNoFocus: {howManyHasNoFocus}, allWindows_len: {len(windows)}")
        if howManyHasNoFocus == len(windows):
            print("All windows lost their focus!")
            from app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller
            self.windowActionsCaller = AppContainer.container.get(WindowActionsCaller)
            self.windowActionsCaller.hideApp()
