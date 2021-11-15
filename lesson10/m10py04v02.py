class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class WarmBlood:
    pass


class ColdBlood:
    pass


class Cat(WarmBlood):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class HybridOne(Cat, ColdBlood, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"


class HybridTwo(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


print(HybridOne.__mro__)
print(HybridTwo.__mro__)
