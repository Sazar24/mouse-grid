# from app.services.theGrid.grid import GridMaker
# from .services.theGrid.grid import GridMaker
from app.grid import GridMaker
from app.ioc.container.container import AppContainer


if __name__ == '__main__':
    # app = GridMaker()
    app = AppContainer.container.get(GridMaker)
    app.run()
