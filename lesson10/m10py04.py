class User:
    profession = "Goit Student"

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def say_hello_instance(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

    @staticmethod
    def say_hello():
        print("Static method")

    @classmethod
    def my_profession(cls):
        print(f"I am a {cls.profession}")


# # instance_user = User()
# #
# # # instance_user.say_hello()
# # # User.say_hello()
# # instance_user.say_hello_instance()
# # # # User.say_hello_instance() - not working
# # User.say_hello_class()
# # instance_user.say_hello_class()
# #
# # print(instance_user)
# # print(User)
#
# user1 = User(27, "Yehor")
# user2 = User(24, "Vasyl")
#
# user1.say_hello_instance()
# user1.my_profession()
# user2.say_hello_instance()
# user2.my_profession()


class Human:
    name = ''

    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    language = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    value = "Python"


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.name = 'Bob'
p_dev.voice()  # Hello! My name is Bob
p_dev.make_some_code()  # My Programming language is Python

js_dev = JSDeveloper()
js_dev.make_some_code()  # My Programming language is JavaScript


class GrandA:
    gizmo = "alpha"


class GrandB:
    gizmo = "beta"


class A(GrandA):
    x = 'I am A class'


class B(GrandB):
    x = 'I am B class'
    y = 'I exist only in B'


class C(B, A):
    z = "This exists only in C"


class D(A, B):
    q = "This exists only in D"


c = C()
d = D()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am B class
print(c.gizmo)  # beta
print(d.gizmo)  # alpha
