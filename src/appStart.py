# from app.services.theGrid.grid import GridMaker
# from .services.theGrid.grid import GridMaker
from app.grid import App
from cwdSetter import CWDSetter
from app.ioc.container.container import AppContainer


if __name__ == '__main__':
    # app = GridMaker()
    CWDSetter.setAppSrcAbsolutePathAsCurrentWorkingDir()
    app = AppContainer.container.get(App)
    app.run()
