# import pynput
# https://pynput.readthedocs.io/en/latest/keyboard.html

# from __future__ import annotations
# from typing import TYPE_CHECKING
from pynput import keyboard
# if TYPE_CHECKING:
#     from src.app.grid import GridMaker
from src.app.services.theGrid.windowSetter.windowActionsCaller import WindowActionsCaller
import tkinter as tk


class GlobalKeystrokeListerner:
    def __init__(self, tkWindow: tk.Tk):
        self.windowActionsCaller = WindowActionsCaller(tkWindow)
        pass

    def run(self) -> None:
        print("in: GlobalKeystrokeListerner.run")
        self.startListeninig()

    def startListeninig(self) -> None:
        self.listener = keyboard.GlobalHotKeys({
            '<alt>+q': self.windowActionsCaller.hideWindow,
            '<alt>+`': self._appBringerHotkeyPressed
        })
        self.listener.start()
        print("listening...")

    def _appBringerHotkeyPressed(self) -> None:
        print("App bringer has been pressed!")
        self.windowActionsCaller.bringWindowToTop()
        pass
