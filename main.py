class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        print("Shakl yuzasi aniqlanmagan")


class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        super().area()
        print(f"Yuza: {self.width * self.height}")


r1 = Rectangle("Kitob", "qizil", 12, 10)
r1.area()
