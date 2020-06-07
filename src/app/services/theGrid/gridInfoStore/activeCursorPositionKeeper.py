from app.utilities.metaclassSingleton.singleton import SingleInstanceMetaClass


class ActiveCursorPositionKeeper(metaclass=SingleInstanceMetaClass):
    currentPos_x: int
    currentPos_y: int

    def cursor_moveLeft(self, step: int = 1) -> None:
        self.currentPos_x -= step
        self.callMovement()

    def cursor_moveRight(self, step: int = 1) -> None:
        self.currentPos_x += step
        self.callMovement()

    def cursor_moveUp(self, step: int = 1) -> None:
        self.currentPos_y -= step
        self.callMovement()

    def cursor_moveDown(self, step: int = 1) -> None:
        self.currentPos_y += step
        self.callMovement()

    def callMovement(self) -> None:
        from app.services.mouseEmulator.mouseEventsCreator import MouseEventsCreator
        MouseEventsCreator().moveMouse(self.currentPos_x, self.currentPos_y)
