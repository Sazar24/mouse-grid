from injector import Injector, inject, singleton
from .dataKeeper import DataKeeper


class Reader:
    @inject
    def __init__(self, dataKeeper: DataKeeper):
        # self.dataToRead =
        self.dataKeeper = dataKeeper

    def read(self):
        print(self.dataKeeper.data)

    def showDataInstance(self):
        return self.dataKeeper
