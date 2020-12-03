from injector import inject, singleton


@singleton
class OnWindowDrawing:
    @inject
    def __init__(self):
        pass

    def drawOnActiveWindow(self):
        pass
