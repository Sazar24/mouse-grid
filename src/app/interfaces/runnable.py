# from interface import interface
from interface import interface


# class IRunnable(interface):  # type: ignore
class IRunnable(interface):
    def run(self) -> None:
        pass
