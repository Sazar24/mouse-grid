mouse-grid-sceleton. (with some proof-of-concept)
Przepisany z pamięci

Sprawdzone mypy, lintowanie. Interfejsy coś nie trybią.


#### 
Poniżej notki własne, puzzle


###
set PYTHONDONTWRITEBYTECODE=1

### 
Prawdopodbnie uproszczeczenie nasłuchiwania na global-hotkeye:
https://stackoverflow.com/questions/50570446/python-tkinter-hide-and-show-window-via-hotkeys


###
creating exe-file:
https://datatofish.com/executable-pyinstaller/
https://www.freehackers.org/Packaging_a_python_program#Py2exe
https://anthony-tuininga.github.io/cx_Freeze/
https://pypi.org/project/cx-Freeze/

###
tkinter tutorial:
https://realpython.com/python-gui-tkinter
https://effbot.org/tkinterbook/canvas.htm
http://zetcode.com/tkinter/drawing/


###
show/hide window:
https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/
https://stackoverflow.com/questions/50570446/python-tkinter-hide-and-show-window-via-hotkeys

####
mypy:
https://mypy.readthedocs.io/en/stable/kinds_of_types.html

####
key-listener:
https://pynput.readthedocs.io/en/latest/keyboard.html
-> ctrl+f: "with keyboard.GlobalHotKeys"



####
workaround na uniknięcie circular-importów - przy typowaniu

# source: https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.grid import GridMaker

### 
multiple-screens:
- link do sprawdzenia:
https://stackoverflow.com/questions/43289364/python-multiple-screen-manipulation-using-tkinter 
- 
https://stackoverflow.com/questions/30312875/tkinter-winfo-screenwidth-when-used-with-dual-monitors

- rozwiązanie doraźne, obejście problemu: Mogę przenosić okno (logoWin+left/right(arrow)) i przy każdym wywołaniu klika obliczać obecną pozycję aktywnegoKwadratu na danym monitorze.
    -- To może być pomocne:
    https://stackoverflow.com/questions/20708138/tkinter-how-can-i-determine-the-position-of-a-toplevel

-

### .py to .exe
https://anthony-tuininga.github.io/cx_Freeze/
- Wolne działanie exe:
https://www.reddit.com/r/Python/comments/9ijnsd/pyinstaller_onefile_exe_is_really_slow/
cxfreeze 
Nuitka