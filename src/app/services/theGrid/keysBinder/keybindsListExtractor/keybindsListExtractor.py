from injector import inject
import json


@inject
class KeybindsListExtractor:
    def __init__(self):
        pass

    def readParams(self):
        # self.__openFile()
        pass

    def __openFile(self):
        """
        # source: https://stackoverflow.com/questions/43601986/how-do-i-read-json-content-from-python-file-that-i-have-made-into-an-executable
        You should've used the full path to the .json file before you compiled it. -- inaczej się wywali przy odpalaniu .exe
        --
        raczej to (powyższe zczyta zahardkodowaną ściężkę, nie pobiera jej przy deployu):
        https://stackoverflow.com/questions/42100198/include-a-json-file-with-exe-pyinstaller
        """
        relativePath: str = "src/keybindings/keybinds.json"
        # fileRawContent = open(relativePath)
        fullPath: str = "C://projects//python//mouse-grid//src//keybindings//keybinds.json"
        fileRawContent = open(fullPath)
        fileTxtContent = fileRawContent.read()
        result = json.loads(fileTxtContent)
        print(result["keybinds"])

    def __parseFileToJson(self):
        pass

    def __getJson(self):
        pass
