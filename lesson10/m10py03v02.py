class Parent:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Hi! My name is {self.name}.")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


child = Child('Joe', 15)
child.say_name()
