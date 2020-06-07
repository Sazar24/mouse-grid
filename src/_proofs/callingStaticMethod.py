class SomeClass:
    innerNumber = 10

    def showNr(self):
        print(self.innerNumber)

    @classmethod
    def increaseAndShowNr(cls):
        cls.innerNumber += 100
        print(cls.innerNumber)

    def sthElse(self):
        self.innerNumber = 44


if __name__ == "__main__":
    print("----start---- ")
    mc = SomeClass()

    mc.showNr()
    SomeClass.increaseAndShowNr()
    mc.showNr()
    SomeClass.increaseAndShowNr()
    mc.showNr()
    print("sthElse....")
    mc.sthElse()
    SomeClass.increaseAndShowNr()
    mc.showNr()
    SomeClass.increaseAndShowNr()
    mc.showNr()

    print(f"instance: {mc.innerNumber}")
    print(f"cls: {SomeClass.innerNumber}")
