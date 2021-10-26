# container extension
from collections import UserDict, UserList


class Phones(UserList):
    def add(self, value):
        self.data.append("+38" + value)

    def get_operator_codes(self):
        codes = []
        for phone in self.data:
            codes.append(phone[3:6])
        return codes


class User(UserDict):
    def get_name(self):
        return self.data["name"]

    def add_phone(self, phone):
        phones = self.data.get("phones", Phones())
        phones.add(phone)
        self.data["phones"] = phones

        # if "phones" not in self.data:
        #     phones = []
        # else:
        #     phones = self.data["phones"]

    def get_phones(self):
        return self.data["phones"]


user = User()
user["name"] = "Bob"
print(user)

print(user.get_name())

user.add_phone("11 222 444")
user.add_phone("333 44 55")
print(user.get_phones())
print(user)
print(user["phones"])

phones = Phones()
phones.add("098 123 45 67")
phones.add("099 123 45 67")

print(phones.get_operator_codes())
print(phones)


# create classes
class EasyUser:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hi! I am {self.name}. I am {self.age} years old.")


# user1 = EasyUser(age=15)
# user1.name = "Bob"
#
#
# user2 = EasyUser("Alice", 20)
#
# user1.say_hello()
# user2.say_hello()


# inheritance
class Person:
    name = ""

    def set_name(self, value):
        self.name = value

    def say_hello(self):
        return f"Hello! I am {self.name}"


class Manager(Person):
    def give_order(self):
        hello_string = self.say_hello()
        return f"{hello_string}. Do your job!"


class Developer(Person):
    def write_code(self):
        return "some code here"


class TeamLead(Manager, Developer):
    def give_order(self):
        return f"Write code!"


# manager = Manager()
# manager.set_name("Bill")
#
# print(manager.say_hello())
# print(manager.give_order())
#
# team_lead = TeamLead()
# team_lead.set_name("Alice")
#
# print(team_lead.write_code())
# print(team_lead.give_order())
