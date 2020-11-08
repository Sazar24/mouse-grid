from typing import Tuple


class Rectangle():
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.__calcBotRightCornerPointPosition()

    def __call__(self) -> Tuple[int, int, int, int]:
        return self.x, self.y, self.x2, self.y2

    def __calcBotRightCornerPointPosition(self):
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

    def __iter__(self):
        return iter((self.x, self.y, self.x2, self.y2))

    def __str__(self) -> str:
        txt = f"Rectangle: x: {self.x}, y: {self.y}, x2: {self.x2}, y2: {self.y2}, width: {self.width}, height: {self.height}."
        return txt
