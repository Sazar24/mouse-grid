from injector import inject
from app.modes.models.rectangle import Rectangle
from app.modes.models.point import Point


class CellMidFinder:
    @inject
    def __init__(self):
        pass

    def findMidPoint(self, cell: Rectangle) -> Point:
        cellWidth: int = cell.x2 - cell.x
        cellHeight: int = cell.y2 - cell.y

        halfOfWidth: int = round(cellWidth / 2)
        halfOfHeight: int = round(cellHeight / 2)

        midPoint_x: Point = cell.x + halfOfWidth
        midPoint_y: Point = cell.y + halfOfHeight

        midPoint = Point(midPoint_x, midPoint_y)
        return midPoint
