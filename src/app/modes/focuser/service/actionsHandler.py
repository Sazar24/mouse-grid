# from injector import inject
# from app.modes.models.rectangle import Rectangle
# from app.modes.models.enums.innerPartRelativePosition import InnerPartRelativePosition_enum
# from app.modes.models.point import Point
# from app.services.mouseHandler.mouseHandler import MouseHandler


# class ActionHandler:
#     @inject
#     def __init__(self,
#                 #  gridColorKeeper: GridColorKeeper,
#                  cellsPositionCalculator: CellsPositionCalculator,
#                  cellMidFinder: CellMidFinder,
#                  mouseHandler: MouseHandler
#                  ):
#         self.color = gridColorKeeper.getActiveColor()
#         self.cellsPositionCalculator = cellsPositionCalculator
#         self.cellMidFinder = cellMidFinder
#         self.mouseHandler = mouseHandler

#     def zoomToRegion(self, activeCell: Rectangle, zoomDirecion: InnerPartRelativePosition_enum):
#         pass
