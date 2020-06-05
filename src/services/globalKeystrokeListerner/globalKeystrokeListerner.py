# import pynput
# https://pynput.readthedocs.io/en/latest/keyboard.html

from pynput import keyboard
from typing import Callable


class GlobalKeystrokeListerner:
    def run(self) -> None:
        print("in: GlobalKeystrokeListerner.run")
        self.startListeninig()

    def startListeninig(self) -> None:
        self.listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+h': self._on_activate_h,
            '<ctrl>+<alt>+i': self._on_activate_i,
            '<alt>+`': self._appBringerHotkeyPressed
        })
        self.listener.start()
        print("listening...")

    def _on_activate_h(self) -> None:
        print('<ctrl>+<alt>+h pressed')
        self.listener.stop()

    callOn_i_: Callable[..., None]

    def _on_activate_i(self) -> None:
        print('<ctrl>+<alt>+i pressed')
        self.callOn_i_()

    def _appBringerHotkeyPressed(self) -> None:
        print("App bringer has been pressed!")
        pass
