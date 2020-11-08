import json


class KwKeeper:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def getArgsAndKwargs(self):
        return self.args, self.kwargs
        # t: str = str(self.kwargs)
        # t = t.replace("':", "'=")
        # result = json.loads(t)
        # return result

    def showMe(self):
        print(self.kwargs)

    def __call__(self):
        return self.getArgsAndKwargs()
