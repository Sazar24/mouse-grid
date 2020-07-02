from injector import inject
import json


class KeybindsListExtractor:
    @inject
    def __init__(self):
        pass

    def readParams(self):
        self.__openFile()
        pass

    def __openFile(self):
        fileRawContent = open("src//keybindings//keybinds.json")
        fileTxtContent = fileRawContent.read()
        result = json.loads(fileTxtContent)
        print(result["keybinds"])

    def __parseFileToJson(self):
        pass

    def __getJson(self):
        pass
