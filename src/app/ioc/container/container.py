from injector import Injector
# import srcmetaclassSingleton.singleton
from app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass


# class Container():
# class AppContainer(metaclass=SingleInstanceMetaClass):
class AppContainer:
    container = Injector()

    # def __init__(self):
    #     self.container: Injector = Injector()
    #     pass

    # def initialize(self):
    #     self.container
    #     pass
