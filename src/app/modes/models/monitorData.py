from typing import Any
from screeninfo.common import Monitor


class MonitorData:
    """
    Klasa niepotrzebna. PyCharm ogarnia typowanie (właśc. importowanie typów) lepiej
    niż vscode. W pyCharm nie muszę tworzyć ręcznie typu, mogę podpiąć się do biblioteki.
    """
    def __init__(self, data: Monitor):
        data.x
        pass
