from injector import inject
from typing import Tuple
from app.modes.models.rectangle import Rectangle
from app.modes.models.enums.innerPartRelativePosition import InnerPartRelativePosition_enum
from app.modes.focuser.service.cellMidFinder import CellMidFinder
from app.modes.models.point import Point


class CellsPositionCalculator:
    @inject
    def __init__(self, cellMidFinder: CellMidFinder):
        self.cellMidFinder = cellMidFinder

    def calcNewPosition(self, parentCell: Rectangle, pickDirection: InnerPartRelativePosition_enum) -> Rectangle:
        topLeftChildRectangle: Rectangle
        topRightChildRectangle: Rectangle
        botLeftChildRectangle: Rectangle
        botRightChildRectangle: Rectangle
        topLeftChildRectangle, topRightChildRectangle, botLeftChildRectangle, botRightChildRectangle = self.divideParentCell(parentCell)

        if pickDirection == InnerPartRelativePosition_enum.topLeft:
            result = topLeftChildRectangle
        elif pickDirection == InnerPartRelativePosition_enum.topRight:
            result = topRightChildRectangle
        elif pickDirection == InnerPartRelativePosition_enum.botLeft:
            result = botLeftChildRectangle
        elif pickDirection == InnerPartRelativePosition_enum.botRight:
            result = botRightChildRectangle
        else:
            raise Exception("Incorrect enum value passed.")

        print("picked rectangle: ")
        print(result())
        return result

    def divideParentCell(self, parentCell: Rectangle) -> Tuple[Rectangle, Rectangle, Rectangle, Rectangle]:
        """ We are going to divide parent grids cell into for smaller cells. """
        width: int = round(parentCell.width / 2)
        height: int = round(parentCell.height / 2)
        midPoint = self.cellMidFinder.findMidPoint(parentCell)

        topLeftChildRectangle = Rectangle((midPoint.x - width), (midPoint.y - height), width, height)
        topRightChildRectangle = Rectangle(midPoint.x, (midPoint.y - height), width, height)
        botLeftChildRectangle = Rectangle((midPoint.x - width), midPoint.y, width, height)
        botRightChildRectangle = Rectangle(midPoint.x, midPoint.y, width, height)

        return topLeftChildRectangle, topRightChildRectangle, botLeftChildRectangle, botRightChildRectangle
