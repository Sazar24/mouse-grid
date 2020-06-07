import tkinter as tk


class WindowParamSetter:
    def setParams(self, tkWindowObject: tk.Tk) -> None:
        self.tkWindowObject: tk.Tk = tkWindowObject

        self._makeWindowTransparent()
        self._makeWindowFullscreen()
        self._setAppTitle()
        # self._removeTitleBar(tkWindowObject)
        pass

    def _makeWindowFullscreen(self) -> None:
        self.tkWindowObject.wm_attributes('-fullscreen', 'true')

        pass

    def _makeWindowTransparent(self) -> None:
        self.tkWindowObject.attributes('-transparentcolor', self.tkWindowObject['bg'])
        pass

    # def _removeTitleBar(self, tkWindowObject: tk.Tk) -> None:
        # tkWindowObject.overrideredirect(1)
        # tkWindowObject.wm_attributes('-type', 'splash')
        # tkWindowObject.wm_attributes('-fullscreen', 'true')

    def _setAppTitle(self) -> None:
        self.tkWindowObject.title("mouse-grid")
