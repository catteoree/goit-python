class Human:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human, name: {self.name}, age: {self.age}"


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        print('I am Man!')


bob = Human('Bob', 20)
print(bob)
man = Man('Bob', 20)
print(bob, man)
