class Human:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"Human, name: {self.name}, age: {self.age}"


bob = Human('Bob', 20)
print(bob)
