import json


class KwKeeper:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def getKwargs(self):
        t: str = str(self.kwargs)
        t = t.replace("':", "'=")
        result = json.loads(t)
        return result

    def showMe(self):
        print(str(self.kwargs))

    def __call__(self):
        return self.getKwargs()


if __name__ == "__main__":
    kwargs1 = KwKeeper(dupa='dupax', foo="bar")
    kwargs1.showMe()
    print(kwargs1.getKwargs())
    print(kwargs1)
