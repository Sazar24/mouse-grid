from injector import inject, singleton
from app.services.handlingMultiScreen.storages.WindowsStore import WindowsStore
from app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller


@singleton
class FocusedScreenManager:
    @inject
    def __init__(self,
                 windowsStore: WindowsStore,
                 windowActionsCaller: WindowActionsCaller
                 ):
        self.windowsStore = windowsStore
        self.windowActionsCaller = windowActionsCaller
        self.activeScreenNumericId = 0

    def setScreen_focuseIn(self, screenNumericId: int):
        self.activeScreenNumericId = screenNumericId
        # for screen in self.windowsStore.getWindows():
        #     screen.

    def setScreen_focusedOut(self):
        """ window can lost focus in many ways.
        We have to capture outside-this-program events."""
        pass
