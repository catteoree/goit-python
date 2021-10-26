# 01
class Animal:
    pass


animal = Animal()


# 02
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


animal = Animal("Milky", 20)


# 03
class Animal:

    def __init__(self, nickname, weight, color="white"):
        self.nickname = nickname
        self.weight = weight
        self.color = color

    def say(self):
        pass

    def change_color(self, color):
        self.color = color


animal = Animal("Simon", 10)
animal.change_color("red")


# 04
class Animal:
    color = 'white'

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_color(self, color):
        self.color = color


class Cat(Animal):
    age = 1

    def say(self):
        return f"Meow"

    def set_age(self, age):
        Cat.age = age


# 05
class Animal:
    color = 'white'

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_color(self, color):
        self.color = color


class Cat(Animal):
    age = 1
    breed = 'British'

    def say(self):
        return 'Meow'

    def set_age(self, age):
        self.age = age


class Dog(Animal):
    age = 2
    breed = 'Haski'

    def __init__(self, nickname, weight, age):
        self.nickname = nickname
        self.weight = weight
        self.age = age

    def say(self):
        return 'Bark'

    def set_age(self, age):
        self.age = age


class Creature(Cat, Dog):
    def total_age(self):
        return Cat.age + self.age


# 06
from collections import UserString


class NumberString(UserString):

    def number_count(self):
        count = 0
        for i in self.data:
            if i.isdigit():
                count += 1
        return count


# 07
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id[:2] != "01":
        raise IDException


# 08
class Animal:

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def get_weight(self):
        return self.weight


class Cat(Animal):
    age = 1
    weight = 5

    def say(self):
        return 'Meow'

    def set_age(self, age):
        self.age = age


def overweight(animal):
    return animal.get_weight() > 10
