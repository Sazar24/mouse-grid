# example source: https://www.pythonprogramming.in/singleton-class-using-metaclass-in-python.html

class SingleInstanceMetaClass(type):
    def __init__(self, name, bases, dic):
        self.__single_instance = None
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if cls.__single_instance:
            return cls.__single_instance
        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwargs)
        cls.__single_instance = single_obj
        return single_obj


# class Dupa(metaclass=SingleInstanceMetaClass):
#     a: int = 13

#     def __init__(self):
#         pass
#     pass


# d1 = Dupa()
# d2 = Dupa()
# print(d1 is d2)

# d1.a = 15
# print(d1 is d2)
# print(d1.a)
# print(d2.a)
# print(d1 is d2)
