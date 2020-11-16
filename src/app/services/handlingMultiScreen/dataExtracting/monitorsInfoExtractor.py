from typing import List
from injector import inject
import screeninfo


@inject
class ScreensInfoExtractor:
    # monitors: List[screeninfo.common.Monitor] = []

    def __init__(self):
        self.monitors: List[screeninfo.common.Monitor] = []

    def getMonitorsData(self) -> List[screeninfo.common.Monitor]:
        self.monitors = screeninfo.get_monitors()
        print("Monitors:")
        for monitor in self.monitors:
            print(monitor)

        print(f"Total monitors amount: {len(self.monitors)}.")
        return self.monitors
