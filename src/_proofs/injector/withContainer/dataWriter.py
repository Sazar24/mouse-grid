from injector import Injector, inject, singleton
from .dataKeeper import DataKeeper


class Writer:
    @inject
    def __init__(self, dataKeeper: DataKeeper):
        self.dataKeeper = dataKeeper

    def write(self, newValue):
        self.dataKeeper.data = newValue

    def showDataInstance(self):
        return self.dataKeeper
