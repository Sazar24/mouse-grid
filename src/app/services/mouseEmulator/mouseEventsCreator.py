from typing import List, Tuple
from pynput.mouse import Controller, Button
# docs-source: https://pynput.readthedocs.io/en/latest/mouse.html#controlling-the-mouse
from src.app.services.theGrid.gridInfoStore.activeRectangleKeeper import ActiveRectangleKeeper
from src.app.services.theGrid.gridInfoStore.activeCursorPositionKeeper import ActiveCursorPositionKeeper


class MouseEventsCreator:
    def __init__(self):
        self.activeRectangleKeeper = ActiveRectangleKeeper()
        self.mouseHandler = Controller()
        self.activeCursorPositionKeeper = ActiveCursorPositionKeeper()

    def moveMouseToGridActiveRectangleCenter(self):
        activeRectangleCoords: List[Tuple[int, int]] = self.activeRectangleKeeper.getActiveRectangleCoords()
        rectanglePoints: List[Tuple[int, int]] = self.activeRectangleKeeper.getActiveRectangleCoords()

        rectangleCornerPoint_topLeft: Tuple[int, int] = rectanglePoints[0]
        rectangleCornerPont_topRight: Tuple[int, int] = rectanglePoints[1]
        rectangleCornerPoint_bottomRight: Tuple[int, int] = rectanglePoints[2]
        rectangleCornerPoint_bottomLeft: Tuple[int, int] = rectanglePoints[3]

        rectangleWidth: int = rectangleCornerPont_topRight[0] - rectangleCornerPoint_topLeft[0]
        rectangleHeight: int = rectangleCornerPoint_bottomLeft[1] - rectangleCornerPoint_topLeft[1]
        centerPoint_x: int = rectangleCornerPoint_topLeft[0] + (rectangleWidth // 2)
        centerPoint_y: int = rectangleCornerPoint_topLeft[1] + (rectangleHeight // 2)
        self.activeCursorPositionKeeper.currentPos_x = centerPoint_x
        self.activeCursorPositionKeeper.currentPos_y = centerPoint_y

        centerPoint: Tuple[int, int] = (centerPoint_x, centerPoint_y)
        print("moving to: " + str(centerPoint))
        # self.mouseHandler.position = (centerPoint_x, centerPoint_y)
        self.mouseHandler.position = (centerPoint)

    def sendClick(self):
        self.mouseHandler.click(Button.left)

    def moveMouse(self, x: int, y: int):
        self.mouseHandler.position = (x, y)
