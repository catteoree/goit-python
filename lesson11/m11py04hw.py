# 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 2
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value


# 3
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        try:
            if x == int(x) or x == float(x):
                self.__x = x
        except ValueError:
            print("x not is a number")
            x = None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        try:
            if y == int(y) or y == float(y):
                self.__y = y
        except ValueError:
            print("y not is a number")
            y = None


# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
