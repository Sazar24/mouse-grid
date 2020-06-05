from interface import implements, Interface


class MyInterface(Interface):  # type: ignore

    def method1(self, x) -> None:
        pass

    def method2(self, x, y) -> None:
        pass


class MyClass(implements(MyInterface)):

    def method1(self, x) -> None:
        return x * 2

    def method2(self, x, y) -> None:
        return x + y
