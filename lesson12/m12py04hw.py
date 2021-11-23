# 1
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as fh:
        unpacked = pickle.load(fh)

    return unpacked


# 2
import json


def write_contacts_to_file(filename, contacts):
    print(contacts)
    data = {}
    print(data)
    data['contacts'] = contacts
    with open(filename, 'w') as fh:
        json.dump(data, fh)


def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        unpacked_data = json.load(fh)
    return unpacked_data['contacts']


# 3
import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = list(contacts[0].keys())
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        contacts = []
        for column in reader:
            contacts.append({
                'name': column['name'],
                'email': column['email'],
                'phone': column['phone'],
                'favorite': column['favorite'] == 'True',
            })
        return contacts


# 4
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename

        if contacts is None:
            contacts = []

        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)

    def read_from_file(self):
        with open(self.filename, 'rb') as fh:
            unpacked = pickle.load(fh)

        return unpacked


# 5
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['count_save'] += 1
        return attributes


# 6
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


# 7
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    person_copy = copy.copy(person)
    return person_copy


# 8
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


# 9
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return Person(self.name, self.email, self.phone, self.favorite)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        return Contacts(self.filename, self.contacts)

    def __deepcopy__(self, memo: dict):
        deep_copy_object = Contacts(copy.deepcopy(self.filename), copy.deepcopy(self.contacts))
        memo[id(deep_copy_object)] = deep_copy_object
        return deep_copy_object


if __name__ == '__main__':
    contacts = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]

    persons = Contacts("user_class.dat", contacts)

    print(persons.contacts[0].name)

    persons.save_to_file()
    person_from_file = persons.read_from_file()
    print(persons == person_from_file)  # False
    print(persons.contacts[0] == person_from_file.contacts[0])  # False
    print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
    print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
    print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
