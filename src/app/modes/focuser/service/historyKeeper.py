from typing import List
from injector import inject, singleton
from app.modes.models.rectangle import Rectangle


@singleton
class HistoryKeeper:
    storyPointer: int = 0
    rootCell: Rectangle

    @inject
    def __init__(self):
        self.movesMade: List[Rectangle] = []

    def getLastMove(self, stepsAmount: int = 1) -> Rectangle:
        lastMoveIndex = len(self.movesMade) - 1 - stepsAmount
        if lastMoveIndex < 0:
            raise Exception("There is no move in history to extract")

        lastMove: Rectangle = self.movesMade[lastMoveIndex]
        return lastMove

    def rememberMove(self, cell: Rectangle):
        self.movesMade.append(cell)

    def setRootCell(self, cell: Rectangle):
        if len(self.movesMade) <= 0:
            self.movesMade.append(cell)
        else:
            self.movesMade[0] = cell
        self.rootCell = cell

    def clearHistory(self):
        self.movesMade = [self.rootCell]

    def getOlderMove(self) -> Rectangle:
        olderMove: Rectangle = self.__popOrGetRoot()
        return olderMove

    def __popOrGetRoot(self) -> Rectangle:
        try:
            result = self.movesMade[-2]
            self.movesMade.pop()
            return result
        except IndexError:
            self.movesMade = [self.rootCell]
            result = self.rootCell
            return result

    def getRootCell(self) -> Rectangle:
        if len(self.movesMade) < 1:
            raise Exception("There is no history to extract (No root cell saved).")
        return self.rootCell

    def removeUndoneMovesFromHistory(self) -> None:
        index: int = self.storyPointer
        # if index >
        self.movesMade = self.movesMade[:index]
        print("removeUndoneMovesFromHistory")
        for i, move in enumerate(self.movesMade):
            print(f"{i}: {move}")

        print("--end of removeUndoneMovesFromHistory")
