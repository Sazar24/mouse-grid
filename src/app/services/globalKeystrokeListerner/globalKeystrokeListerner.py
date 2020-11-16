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
from app.services.theGrid.windowSetter.masterWindowInstanceKeeper import masterWindowInstanceKeeper
from app.ioc.container.container import AppContainer


@inject
class GlobalKeystrokeListerner:
    def __init__(self, windowKeeper: masterWindowInstanceKeeper):
        window = windowKeeper.getWindow()
        self.windowActionsCaller = AppContainer.container.get(WindowActionsCaller)

    def run(self) -> None:
        self.__startListeninig()

    def __startListeninig(self) -> None:
        self.listener = keyboard.GlobalHotKeys({
            '<alt>+q': self.windowActionsCaller.hideApp,
            '<alt>+`': self.__appBringerHotkeyPressed,
            '<shift>+<esc>': self.__quitProgram,
        })
        self.listener.start()
        print("listening...")

    def __appBringerHotkeyPressed(self) -> None:
        print("App bringer has been pressed!")
        self.windowActionsCaller.bringAppToTop()

    def __quitProgram(self) -> None:
        print("Wywołano zakończenie programu.")
        self.windowActionsCaller.terminateProgram()
        print("...bye bye.")
