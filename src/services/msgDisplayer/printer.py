from typing import Any


class Printer:
    deepMsg: str = "I-am-prrriiiiinteeeer!"

    def showText(self, text: str) -> None:
        """
        sdfdsfsfd
        """
        print(text)

    def showNr(self, number: int) -> None:
        print(number)

    def dupa(self) -> Any:
        pass


Printer().showText("dfs")
