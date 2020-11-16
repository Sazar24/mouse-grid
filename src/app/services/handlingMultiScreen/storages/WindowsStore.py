from injector import inject, singleton
from typing import List
from app.services.handlingMultiScreen.dataExtracting.monitorsInfoExtractor import ScreensInfoExtractor
from app.services.handlingMultiScreen.screenWindow import ScreenWindow


@singleton
class WindowsStore:
    windowsAmount: int
    __knownWindows: List[ScreenWindow]

    @inject
    def __init__(self, screensInfoExtractor: ScreensInfoExtractor):
        pass

    def update(self, windows: List[ScreenWindow]):
        self.__knownWindows = windows
        self.windowsAmount = len(self.__knownWindows)
        print(f"windows amount: {self.windowsAmount}.")

    def getWindows(self) -> List[ScreenWindow]:
        return self.__knownWindows

    def getWindowByNumericId(self, numericId: int) -> ScreenWindow:
        match: List[ScreenWindow] = list(filter(lambda s: s.id == numericId, self.__knownWindows))
        if len(match) == 0:
            raise Exception(f"There is no window with given numericId: {numericId}.")
        if len(match) > 1:
            raise Exception(f"Found more than one result of screen with numericId: {numericId}.")

        result: ScreenWindow = match[0]
        return result
