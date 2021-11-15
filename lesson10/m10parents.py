class Parent1:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Hi! My name is {self.name}.")


class Parent2:
    def __init__(self):
        print("This is parent2")


class Child(Parent1, Parent2):
    def __init__(self, name, age):
        super(Child, self).__init__(name)
        # super(Parent2, self).__init__()
        self.age = age
        # self.name = name


child = Child("Job", 25)
child.say_name()
# parent2 = Parent2()
# parent2.__init__()
