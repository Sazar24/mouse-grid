from injector import inject, singleton
import screeninfo
from typing import List
from app.services.handlingMultiScreen.monitorsInfoExtractor import ScreensInfoExtractor
from app.services.handlingMultiScreen.screenWindow import ScreenWindow


@singleton
class WindowsStore:
    windowsAmount: int
    knownWindows: List[ScreenWindow]

    @inject
    def __init__(self, screensInfoExtractor: ScreensInfoExtractor):
        pass

    def update(self, windows: List[ScreenWindow]):
        self.knownWindows = windows
        self.windowsAmount = len(self.knownWindows)
        print(f"windows amount: {self.windowsAmount}.")
