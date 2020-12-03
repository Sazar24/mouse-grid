from app.modes.models.rectangle import Rectangle
from app.services.handlingMultiScreen.screenWindow import ScreenWindow


class OnScreenHistoricalPick:
    def __init__(self, screenId: int, rectangle: Rectangle):
        self.screenId = screenId
        self.rectangle = rectangle
