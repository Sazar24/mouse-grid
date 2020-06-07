from app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass
from app.services.theGrid.gridInfoStore.gridLinesCoordsStore import GridLinesCoordsStore
from typing import List, Tuple


class ActiveRectangleKeeper(metaclass=SingleInstanceMetaClass):
    currentRowNr: int = 1
    currentColumnNr: int = 1

    def __init__(self):
        self.coordsStore = GridLinesCoordsStore()
        print("ActiveRectangleKeeper - constructor has been called!")

    def currentRow_down(self, step: int = 1):
        maxRowNr: int = len(self.coordsStore.getAllHorizontalLines()) - 2
        print(f"maxRowNr: {maxRowNr} ,len(self.coordsStore.getAllHorizontalLines()): {len(self.coordsStore.getAllHorizontalLines())} ")
        if (self.currentRowNr + step) <= maxRowNr:
            self.currentRowNr += step
        elif (self.currentRowNr + step) > maxRowNr:
            self.currentRowNr = self.currentRowNr + step - maxRowNr - 1
        print(f"currentRowNr: {self.currentRowNr}")

    def currentRow_up(self, step: int = 1):
        maxRowNr: int = len(self.coordsStore.getAllHorizontalLines()) - 2
        if (self.currentRowNr - step) >= 0:
            self.currentRowNr -= step
        elif(self.currentRowNr - step) < 0:
            # tu robię przeskakiwanie z dolnej krawędzi na górną:
            self.currentRowNr = maxRowNr + (self.currentRowNr - step) + 1
        print(f"currentRowNr: {self.currentRowNr}")

    def currentColumn_left(self, step: int = 1):
        maxColumnNr: int = len(self.coordsStore.getAllVertcicalLines()) - 2
        if (self.currentColumnNr - step) >= 0:
            self.currentColumnNr -= step
        elif (self.currentColumnNr - step) < 0:
            self.currentColumnNr = maxColumnNr + ((self.currentColumnNr - step)) + 1
        print(f"currentColumnNr: {self.currentColumnNr}")

    def currentColumn_right(self, step: int = 1):
        maxColumnNr: int = len(self.coordsStore.getAllVertcicalLines()) - 2
        if (self.currentColumnNr + step) <= maxColumnNr:
            self.currentColumnNr += step
        elif (self.currentColumnNr + step) > maxColumnNr:
            self.currentColumnNr = self.currentColumnNr + step - maxColumnNr - 1
        print(f"currentColumnNr: {self.currentColumnNr}")

    def getActiveRectangleCoords(self) -> List[Tuple[int, int]]:
        # result = (1, 2, 3, 4)
        result = self.__fromGridLinesExtractRectangleCornersCoords()
        return result

    def __fromGridLinesExtractRectangleCornersCoords(self) -> List[Tuple[int, int]]:
        self.__decreaseActiveColumnAndRowIfExceededMax()

        horizontalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllHorizontalLines()
        currentRow_horizontalTopLine = horizontalLines[self.currentRowNr]
        currentRow_horizontalBottomLine = horizontalLines[self.currentRowNr + 1]

        verticalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllVertcicalLines()
        currentColumn_rightLine = verticalLines[self.currentColumnNr + 1]
        currentColumn_leftLine = verticalLines[self.currentColumnNr]

        rectangleCornerPoint_topLeft: Tuple[int, int] = (currentColumn_leftLine[0], currentRow_horizontalTopLine[1])
        rectangleCornerPont_topRight: Tuple[int, int] = (currentColumn_rightLine[0], currentRow_horizontalTopLine[1])
        rectangleCornerPoint_bottomRight: Tuple[int, int] = (currentColumn_rightLine[0], currentRow_horizontalBottomLine[1])
        rectangleCornerPoint_bottomLeft: Tuple[int, int] = (currentColumn_leftLine[0], currentRow_horizontalBottomLine[1])

        allCorners: List[Tuple[int, int]] = [
            rectangleCornerPoint_topLeft,
            rectangleCornerPont_topRight,
            rectangleCornerPoint_bottomRight,
            rectangleCornerPoint_bottomLeft
        ]

        return allCorners

    def __decreaseActiveColumnAndRowIfExceededMax(self):
        """
        Był bug, że zbyt duże pomniejszenie gęstości siatki (gdy aktywnyKwadrat był na pozycji innej niż 0,0)
        powodowało wyjście poza tablicę dostępnych linii wierszy/kolumn.
        Rozwiązanie poniżej jest stosunkowo specyficzne. Wynika to z tego, że w przyszłości prawdopodnie zmienię sposób rysowania grida
        (zwłaszcza ostatnich, skrajnych linii).
        Przed oddaniem wersji końcowej - do poprawy (TODO)
        """
        shouldValidate: bool = True
        while (shouldValidate):
            try:
                horizontalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllHorizontalLines()
                currentRow_horizontalBottomLine = horizontalLines[self.currentRowNr + 1]
                shouldValidate = False
            except IndexError:
                self.currentRowNr -= 1
                shouldValidate = True

            try:
                verticalLines: List[Tuple[int, int, int, int]] = self.coordsStore.getAllVertcicalLines()
                currentColumn_rightLine = verticalLines[self.currentColumnNr + 1]
                shouldValidate = False
            except IndexError:
                self.currentColumnNr -= 1
                shouldValidate = True
