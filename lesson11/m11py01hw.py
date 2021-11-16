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
        self.employees_dict = {n: i for i, n in enumerate(self.surnames)}

    def __setitem__(self, key, value):
        self.value = value
        self.key = key
        self.employees_dict[key] = self.value

    def __getitem__(self, item):
        print(item)
        print(self.employees_dict)
        if item in self.employees_dict.keys():
            return self.employees_dict[item]
        else:
            return None


# 4
class Employees:
    def __init__(self, surnames, group):
        self.employees_dict = {}
        ids = range(0, len(surnames))
        for iterator in range(0, len(surnames)):
            self.employees_dict[surnames[iterator]] = ids[iterator]
        self.group = group

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        return self.employees_dict[item]

    def __call__(self, item):
        for key, value in self.employees_dict.items():
            if item == value:
                return [key]
        return None


# 5
class Client:
    def __init__(self, client_list, discount):
        self.client_list = client_list
        self.discount = discount
        self.current_client = 0

    def __next__(self):
        if self.current_client < len(self.client_list):
            self.current_client += 1
            print(self.current_client)
            return self.client_list[self.current_client - 1]
        raise StopIteration

    def __iter__(self):
        return self


# 6
class Customer:
    def __init__(self, surname, id=1):
        self.__surname = surname
        self.__id = id

    def __add__(self, b):
        return self.id + b.id

    def __repr__(self):
        return f'Customer("{self.surname}", {self.id})'

    def __str__(self):
        return f'customer id = {self.id} and surname is {self.surname}'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def set_surname(self, surname):
        if len(surname):
            self.__surname = surname

    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self, id):
        if id:
            self.__id = id


# 7
class Customer:
    def __init__(self, surname, id=1):
        self.__surname = surname
        self.__id = id

    def __add__(self, b):
        return self.id + b.id

    def __repr__(self):
        return f'Customer("{self.surname}", {self.id})'

    def __str__(self):
        return f'customer id = {self.id} and surname is {self.surname}'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def set_surname(self, surname):
        if len(surname) > 0:
            self.__surname = surname

    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self, id):
        if id > 0:
            self.__id = id

    def __eq__(self, other):
        if self.__id == other.__id and self.__surname == other.__surname:
            return True
        return False

    def __ne__(self, other):
        if self.__id != other.__id or self.__surname != other.__surname:
            return True
        return False

    def __gt__(self, other):
        if self.__id > other.__id:
            return True
        return False

    def __lt__(self, other):
        if self.__id < other.__id:
            return True
        return False

    def __ge__(self, other):
        if self.__id >= other.__id:
            return True
        return False

    def __le__(self, other):
        if self.__id <= other.__id:
            return True
        return False


# 8
class FoodComponent:
    def __init__(self, product_names, weight, price):
        self.product_names = product_names
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'Product {str(self.product_names)}, weight = {self.weight}, price = {self.price}'

    def __add__(self, other):
        self.product_names += other.product_names
        self.weight += other.weight
        self.price += other.price
