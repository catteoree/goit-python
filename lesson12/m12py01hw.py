# 1
import pickle


class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False


def write_object(customer):
    return pickle.dumps(customer)


def write_to_file(customer, path):
    with open(path, 'wb') as fh:
        pickle.dump(customer, fh)


# 2
import json


def write_object(customer):
    return json.dumps(customer)


def write_to_file(customer, path):
    with open(path, 'w') as fh:
        json.dump(customer)


# 3
import csv


def write_customers_to_csv(customers, file_name):
    print(customers)
    with open(file_name, 'w', newline='') as fh:
        field_names = ['id', 'name']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for customer in customers:
            writer.writerow(customer)


# 4
class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] = attributes['id'] * 4
        return attributes


# 5
class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id /= 4


# 6
import copy


class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id /= 4


def create_incremented_customer(customer):
    customer_copy = copy.copy(customer)
    customer_copy.id += 1
    return customer_copy


# 7
import copy


class Customer:
    def __init__(self, surname, id, attributes):
        self.surname = surname
        self.id = id
        self.attributes = attributes

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id /= 4


def create_incremented_customer(customer):
    customer_deep_copy = copy.deepcopy(customer)
    customer_deep_copy.id += 1
    return customer_deep_copy


# 8
from copy import deepcopy, copy


class Customer:
    def __init__(self, surname, id, attributes):
        self.surname = surname
        self.id = id
        self.attributes = attributes

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id /= 4

    def __copy__(self):
        copy_object = Customer(self.surname, self.id, self.attributes)
        copy_object.surname = self.surname
        copy_object.id = self.id
        copy_object.attributes = self.attributes
        return copy_object

    def __deepcopy__(self):
        copy_object = Customer(self.surname, self.id, self.attributes)
        copy_object.surname = deepcopy(self.surname)
        copy_object.id = deepcopy(self.id)
        copy_object.attributes = deepcopy(self.attributes)
        return copy_object


def create_incremented_customer(customer):
    new_customer = customer.__deepcopy__()
    new_customer.id += 1
    return new_customer


if __name__ == '__main__':
    pickle.dumps(Customer('gftyj', '123'))