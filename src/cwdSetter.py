import os
from pathlib import Path
import __main__


class CWDSetter:
    @classmethod
    def setAppSrcAbsolutePathAsCurrentWorkingDir(cls):
        """
        Aplikacja jest uruchamiana komendą 'python src//app.py'.
        Czyli używana jest ścieżka relatywna do bieżącego katologu (w którym aktualnie znajdujemy się w konsoli terminalu).
        (Tzw current-working-dir   -- w skrócie: cwd).
        Aplikacja - zwłaszcza część pythonowa - może być odpalona skądkolwiek, np:
        > c:// > python c://projects//aplikacje//...//src//app.py  (i też zadziała)   // cwd == "c:/"
        Chcemy jednak, żeby aplikacja miała zawsze swoje stałe cwd. Przyda się to chociażby przy tworzeniu katalogów/plików z logami.
        """
        appSrcDir_absolutePath: str = os.path.dirname(os.path.abspath(__main__.__file__))
        properWorkingDir_absolutePath: str = str(Path(appSrcDir_absolutePath).parent)
        print(
            f"__main__: {str(__main__)} | \n"
            f"__main__.__file__ : {str(__main__.__file__)}  |\n"
            f"os.path.abspath(__main__.__file__): {str(os.path.abspath(__main__.__file__))} |\n"
            f"appSrcDir_absolutePath: {appSrcDir_absolutePath}  |\n"
            f"properWorkingDir_absolutePath: {properWorkingDir_absolutePath} \n"
        )
        os.chdir(properWorkingDir_absolutePath)
