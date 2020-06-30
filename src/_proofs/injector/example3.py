from dataclasses import dataclass
from injector import Injector, inject, singleton


# @dataclass
@singleton
class DataKeeper:
    # @singleton
    def __init__(self):
        self.data: int = 0


# @inject
# @dataclass
class Reader:
    @inject
    def __init__(self, dataKeeper: DataKeeper):
        # self.dataToRead =
        self.dataKeeper = dataKeeper

    def read(self):
        print(self.dataKeeper.data)

    def showDataInstance(self):
        return self.dataKeeper


# @inject
class Writer:
    @inject
    def __init__(self, dataKeeper: DataKeeper):
        self.dataKeeper = dataKeeper

    def write(self, newValue):
        self.dataKeeper.data = newValue

    def showDataInstance(self):
        return self.dataKeeper


if __name__ == "__main__":
    container = Injector()
    myReader = container.get(Reader)
    myReader.read()

    myWriter = container.get(Writer)
    myWriter.write(7)
    myReader.read()

    myWriter2 = container.get(Writer)
    myWriter2.write(17)
    myReader.read()

    container2 = Injector()
    reader_from2ndContainer = container2.get(Reader)
    reader_from2ndContainer.read()
    print(myReader.showDataInstance())
    print(myWriter.showDataInstance() is myWriter2.showDataInstance())
    print("-- readers compare:")
    print(myReader.showDataInstance() is reader_from2ndContainer.showDataInstance())
