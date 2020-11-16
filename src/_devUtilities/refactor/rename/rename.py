from rope.base.project import Project
from rope.refactor.rename import Rename


class FileRefactorer:

    def __init__(self):
        pass

    def runRenaming(self):
        self.proj.do(self.change)

    def setProjectFolder(self, folderName):
        self.proj = Project(folderName)
        [f.name for f in self.proj.get_files()]

    def setFileToRename_originalName(self, originalName: str):
        self.fileToRename = self.proj.get_file(originalName)

    def setFileToRename_destinationName(self, wantedResultName: str):
        self.destinationName = wantedResultName
        try:
            self.change = Rename(
                self.proj,
                self.fileToRename
            ).get_changes(wantedResultName)
            # )._rename_module(wantedResultName)
        except FileNotFoundError as err:
            print("\n+++There is no file in given name or path to change its name or path.\n")
            print(err)
        except Exception as err:
            print("\n+++Error while searching file which you wanted to be renamed.\n")
            print(err)

    def reverseRenaming(self):
        pass


if __name__ == "__main__":
    # name1 = "mainGrid/gridDataProvider.py"
    name1 = "mouseGrid/services/gridMaker/app.py"
    name2 = "theMG"
    # name2 = "mainGrid/gridDataProvider.py"

    refactorMaker = FileRefactorer()
    refactorMaker.setProjectFolder("src")
    refactorMaker.setFileToRename_originalName(name1)
    refactorMaker.setFileToRename_destinationName(name2)

    refactorMaker.runRenaming()
