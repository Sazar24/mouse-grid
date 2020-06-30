from injector import Injector, inject, singleton
from src.app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass


class Container(SingleInstanceMetaClass):
    def __init__(self):
        self.config()

    def config(self):
        self.container = Injector()
        pass


