from injector import inject
from pynput.mouse import Controller, Button
from app.modes.models.point import Point


class MouseHandler:
    @inject
    def __init__(self):
        self.mouseController = Controller()

    def moveMouse(self, x: int, y: int):
        self.mouseController.position = (x, y)

    def moveMouseToPoint(self, point: Point):
        self.mouseController.position = (point.x, point.y)

    def click(self):
        self.mouseController.click(Button.left)
