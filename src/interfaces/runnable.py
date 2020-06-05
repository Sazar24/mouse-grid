# from interface import interface
from interface import interface


class IRunnable(interface):  # type: ignore
    def run(self) -> None:
        pass
