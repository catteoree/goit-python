# 1
# class Customer:
#     def __init__(self, surname, id=1):
#         self.surname = surname
#         self.id = id
#
#     def __add__(self, other):
#         return self.id + other.id


# 2
class Customer:
    def __init__(self, surname, id=1):
        self.surname = surname
        self.id = id

    def __add__(self, b):
        return self.id + b.id

    def __repr__(self):
        return f"Customer('{self.surname}', {self.id})"

    def __str__(self):
        return f"customer id = {self.id} and surname is {self.surname}"


# 3
class Employees:
    def __init__(self, surnames, group):
        self.surnames = surnames
        self.group = group
        self.employees_dict = {}

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        if item:
            return self.employees_dict[item]
        else:
            return None




# 4
# 5
# 6
# 7
# 8
