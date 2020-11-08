from injector import inject
from typing import List
from app.services.theGrid.windowSetter.canvasInstanceKeeper import CanvasInstanceKeeper
from app.modes.focuser.service.cellsPositionCalculator import CellsPositionCalculator
from app.services.theGrid.gridInfoStore.gridColorKeeper import GridColorKeeper
from app.modes.models.rectangle import Rectangle
from app.modes.models.point import Point


class CellInnerCrossMaker:
    @inject
    def __init__(self,
                 gridColorKeeper: GridColorKeeper,
                 canvasInstanceKeeper: CanvasInstanceKeeper,
                 cellsPositionCalculator: CellsPositionCalculator
                 ):
        self.canvasInstanceKeeper = canvasInstanceKeeper
        self.colorKeeper = gridColorKeeper
        self.cellsPositionCalculator = cellsPositionCalculator
        self.__inititate()

    def __inititate(self):
        self.canvas = self.canvasInstanceKeeper.getCanvas()
        self.crossLinesColor = self.colorKeeper.getInnerLinesColor()

    def drawPartisionLines(self, parentCell: Rectangle):
        color = self.crossLinesColor
        childRectangles: List[Rectangle] = self.cellsPositionCalculator.divideParentCell(parentCell)

        topXY: Point = Point(childRectangles[0].x2, childRectangles[0].y)
        botXY: Point = Point(childRectangles[2].x2, childRectangles[2].y2)
        leftXY: Point = Point(childRectangles[0].x, childRectangles[2].y)
        rightXY: Point = Point(childRectangles[1].x2, childRectangles[1].y2)

        self.canvas.create_line(*topXY, *botXY, fill=color)
        self.canvas.create_line(*leftXY, *rightXY, fill=color)
