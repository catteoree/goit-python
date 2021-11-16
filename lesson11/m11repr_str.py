class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class HelloPoint(Point):
    def __init__(self, x, y):
        super(HelloPoint, self).__init__(x, y)

    def __str__(self):
        return f'Hello! I am Point({self.x}, {self.y})'


a = Point(1, 9)
b = HelloPoint(2, 4)
print(a)
