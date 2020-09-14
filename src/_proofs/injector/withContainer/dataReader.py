from injector import Injector, inject, singleton
from .dataKeeper import DataKeeper


@inject
class Reader:
    def __init__(self, dataKeeper: DataKeeper):
        self.dataKeeper = dataKeeper

    def read(self):
        print(self.dataKeeper.data)

    def showDataInstance(self):
        return self.dataKeeper
