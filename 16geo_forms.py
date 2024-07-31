class GeoForm:
    def __init__(self):
        pass

    def cal_area():
        pass

    def cal_perimeter():
        pass


class Circle(GeoForm):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def cal_area(self):
        return (self.pi * self.radius) ** 2

    def cal_perimeter(self):
        return (self.pi * 2) * self.radius


class Rectangle(GeoForm):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def cal_area(self):
        return self.lenght * self.width

    def cal_perimeter(self):
        return (self.lenght*2) * self.width


circle = Circle(2)
rectangle = Rectangle(4, 2)

print(circle.cal_area())
print(circle.cal_perimeter())
print(rectangle.cal_area())
print(rectangle.cal_perimeter())
