class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __iter__(self):
        return iter((self.x, self.y))


# class Printer:
#     @staticmethod
#     def show(x, y):
#         print(f"x: {x}, y: {y}")


# if __name__ == "__main__":
#     Printer.show(12, 42)  # output:  x: 12, y: 42

#     p = Point(123, 53)
#     # Printer.show(*p)       # output:  TypeError. ( missing 1  argument) <-- to chcę zmienić.
#     Printer.show(*p)       # desired-output:  x: 123, y: 53

#     # Pytanie:
#     # Jak i którą klasę poprawić, żeby powyższy kod
#     # zwrócił wyniki takie, jak opisano w komentarzach.
