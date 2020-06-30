# import pynput
# https://pynput.readthedocs.io/en/latest/keyboard.html

# from __future__ import annotations
# from typing import TYPE_CHECKING
from injector import inject
import tkinter as tk
from pynput import keyboard
# if TYPE_CHECKING:
#     from app.grid import GridMaker
from app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller
from app.services.theGrid.windowSetter.windowInstanceKeeper import WindowInstanceKeeper
from app.ioc.container.container import AppContainer


class GlobalKeystrokeListerner:
    @inject
    def __init__(self, windowKeeper: WindowInstanceKeeper):
        window = windowKeeper.getWindow()
        self.windowActionsCaller = AppContainer.container.get(WindowActionsCaller)
        pass

    def run(self) -> None:
        print("in: GlobalKeystrokeListerner.run")
        self.__startListeninig()

    def __startListeninig(self) -> None:
        self.listener = keyboard.GlobalHotKeys({
            '<alt>+q': self.windowActionsCaller.hideWindow,
            '<alt>+`': self.__appBringerHotkeyPressed
        })
        self.listener.start()
        print("listening...")

    def __appBringerHotkeyPressed(self) -> None:
        print("App bringer has been pressed!")
        self.windowActionsCaller.bringWindowToTop()
        pass
