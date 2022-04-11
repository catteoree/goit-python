"""Classes for book of user contacts."""

from collections import UserDict
from typing import Optional


class Field:
    """Fields of records in contact book: name, phone/phones, etc."""

    def __init__(self, value: str) -> None:
        self.value = value


class Name(Field):
    """Name of the contact. Only """


class Phone(Field):
    """Phone of the contact."""

    def __eq__(self, other) -> bool:
        """Input object Phone. Return bool."""
        return self.value == other.value

    def __str__(self):
        return f'Phone:{self.value}'


class Record:
    """
    Records (contacts) in users contact book.

    Only one name, but it can be more than one phone.
    """

    def __init__(self, name: str, phone: list[str] = None) -> None:
        """Input 2 arguments. First str, second optional. Return None."""
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(p) for p in phone]
        self.name = Name(name)

    def add_phone(self, phone_number: str) -> None:
        """Input str. Return None."""
        phone = Phone(phone_number)
        if phone not in self.phone:
            self.phone.append(phone)

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phone:
            if p.value == phone:
                return p

    def delete_phone(self, phone: str) -> None:
        """Input str. Return None."""
        phone_to_delete = self.find_phone(phone)
        self.phone.remove(phone_to_delete) if phone_to_delete else None

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Input str. Return None."""
        new_phone = Phone(new_phone)
        phone_to_remove = self.find_phone(old_phone)
        if phone_to_remove:
            self.phone.remove(phone_to_remove)
            self.phone.append(new_phone)

    def __str__(self):
        return f'Record of {self.name.value}, phones {[p.value for p in self.phone]}'

    def __repr__(self):
        return f'Record of {self.name.value}, phones {[p.value for p in self.phone]}'


class AddressBook(UserDict):
    """All contacts data."""

    def add_record(self, record: list) -> None:
        """Input list. Return None."""
        record = Record(record[0], record[1:])
        self.data[record.name.value] = record

    def find_record(self, value: str) -> Optional[Record]:
        """Input str. Return Record(name, phone=None) or None."""
        return self.data.get(value)

    def delete_record(self, value: str) -> None:
        """Input str. Return None."""
        self.data.pop(value)

    def __str__(self):
        return str(self.data)


def main():
    book = AddressBook()
    book.add_record(['Yehor', '0662624554', '0953456787'])
    book.add_record(['Pavel', '0662234554', '0953455487'])

    record = book.find_record('Pavel')
    book.delete_record('Yehor')

    print('#' * 10)
    print(book)
    print(record)

    record.delete_phone('0662234554')
    record.edit_phone('0953455487', '0992624554')

    print('#' * 10)
    print(book)
    print(record)


if __name__ == '__main__':
    main()
