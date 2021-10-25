class Rectangle:
    def __init__(self, s1, s2):
        self.a = s1
        self.b = s2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def __str__(self):
        return "Rectangle object"


def main():
    rec1 = Rectangle(5, 4)
    print(rec1)
    print("Perimeter:", rec1.perimeter())
    print("Square:", rec1.square())

    rec2 = Rectangle(5, 2)
    print(rec2)
    print("Perimeter:", rec2.perimeter())
    print("Square:", rec2.square())


if __name__ == "__main__":
    main()
