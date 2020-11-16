from injector import inject, singleton
import screeninfo
from typing import List
from app.services.handlingMultiScreen.dataExtracting.monitorsInfoExtractor import ScreensInfoExtractor


@singleton
class MonitorsInfoKeeper:
    monitors: List[screeninfo.common.Monitor] = []

    @inject
    def __init__(self, screensInfoExtractor: ScreensInfoExtractor):
        self.screensInfoExtractor = screensInfoExtractor
        self.update()

    def getData(self) -> List[screeninfo.common.Monitor]:
        return self.monitors

    def update(self):
        self.monitors = self.screensInfoExtractor.getMonitorsData()
