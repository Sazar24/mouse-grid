from injector import Injector, inject, singleton


@singleton
class DataKeeper:
    def __init__(self):
        self.data: int = 0
