from cmath import pi


class Figure:
    sides = []

    def area(self):
        return "Some area"

    def get_sides(self):
        return self.sides

    def set_sides(self, list_of_sides):
        self.sides = list_of_sides


class Rectangle(Figure):
    sides = [1, 2]

    def area(self):
        return self.sides[0] * self.sides[1]


class Triangle(Figure):
    pass


class Circle(Figure):
    radius = 5

    def area(self):
        return pi * (self.radius ** 2)


class SomeFigure(Figure):
    sides = [3, 5, 3, 2, 7]


class StrangeFigure(Figure):
    def get_sides(self):
        return super().get_sides()


c = Circle()
print(c.sides)
print(c.radius)
print(c.area())

r = Rectangle()
print(r.sides)
print(r.area())

sf = SomeFigure()
print(sf.sides)
print(sf.area())

strange_f = StrangeFigure()
print(strange_f.get_sides())
