import screeninfo
from injector import inject
from typing import List
from app.services.handlingMultiScreen.dataExtracting.monitorsInfoExtractor import ScreensInfoExtractor
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper
from app.services.handlingMultiScreen.storages.monitorsInfoKeeper import MonitorsInfoKeeper
from app.services.handlingMultiScreen.screenWindow import ScreenWindow
from app.services.handlingMultiScreen.storages.WindowsStore import WindowsStore


class WindowsMaker:
    @inject
    def __init__(self,
                 screensInfoExtractor: ScreensInfoExtractor,
                 masterWindowInstanceKeeper: masterWindowInstanceKeeper,
                 monitorsInfoKeeper: MonitorsInfoKeeper,
                 windowsStore: WindowsStore,
                 ):
        self.masterWindowInstanceKeeper = masterWindowInstanceKeeper
        # self.screensInfoExtractor = screensInfoExtractor
        self.monitorsInfoKeeper = monitorsInfoKeeper
        self.windowsStore = windowsStore

    def run(self):
        self._makeWindows()

    def _makeWindows(self):
        self.__buildAllWindows()

    def __buildAllWindows(self):
        self.getParentWindow()
        self.getDataAbountMonitors()
        self.forEachMonitorBuildWindow()

    def getParentWindow(self):
        self.parentWindow = self.masterWindowInstanceKeeper.getWindow()

    def getDataAbountMonitors(self):
        self.screensData: List[screeninfo.common.Monitor] = self.monitorsInfoKeeper.getData()

    def forEachMonitorBuildWindow(self):
        allWindows: List[screeninfo.common.Monitor] = []

        for nth, screen in enumerate(self.screensData):
            numericId: int = nth + 1  # we want to aviod 0 value.
            newWindow = ScreenWindow(self.parentWindow, screen, numericId)
            allWindows.append(newWindow)

        self.windowsStore.update(allWindows)
