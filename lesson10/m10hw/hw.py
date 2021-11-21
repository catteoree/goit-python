from collections import UserDict


class Field:
    def __init__(self, name, *args, **kwargs):
        if isinstance(name, Name):
            self.name = name.value
        else:
            self.name = name
        self.value = None
        if args and kwargs:
            self.value = [list(args) if len(args) > 1 else args[0], kwargs]
        elif args:
            self.value = list(args) if len(args) > 1 else args[0]
        elif kwargs:
            self.value = kwargs

    def __repr__(self):
        return f'{self.name}: {self.value}'


class Name(Field):
    def __init__(self, name: str):
        self.value = name

    def __repr__(self):
        return f'{self.value}'


class Phone(Field):
    def __init__(self, *args, name='phone'):
        super().__init__(name, *args)
        phones = list(args)

        if len(phones) > 1:
            self.value = phones
        else:
            self.value = phones[0]


class Record:
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.value = None
        self.data = {}

        if phone:
            self.value = {}
            self.value[phone.name] = phone.value

        self.data[self.name.value] = self.value
        self.record_name = self.data[self.name.value]

    def __repr__(self):
        return f'{self.name.value}: {self.value}'

    def add_field(self, field: Field):
        if field.name not in self.record_name:
            self.record_name[field.name] = field.value
            return f'Field with name \"{field.name}\" ' \
                   f'and \"{field.value}\" is added successfully'
        else:
            return f'This field with name \"{field.name}\" exists.'

    def delete_field(self, field: Field):
        if field.name in self.record_name:
            self.record_name.pop(field.name)
            return f'Field with name: \"{field.name}\" ' \
                   f'and value: \"{field.value}\" is deleted successfully'
        else:
            return f'This field with name \"{field.name}\" not exist.'

    def edit_field(self, field: Field):
        if field.name in self.record_name:
            old_value = self.record_name[field.name]
            self.record_name[field.name] = field.value
            return f'Field with name: \"{field.name}\" and old value: ' \
                   f'\"{old_value}\" changed to \"{field.value}\" successfully'
        else:
            return f'This field with name \"{field.name}\" not exist.'


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            return f'Record with name: \"{record.name.value}\" exists.'
        self.data[record.name.value] = record.value
        return f'Record with name: \"{record.name.value}\" ' \
               f'and value: \"{record.value}\" is added successfully'


def main():
    a = AddressBook()
    f = Field('new_phone', '0501234566')
    f2 = Field('only_name')
    new_f2 = Field('only_name', 'not_only_name', pet='cat')
    new_f3 = Field("it\'s", test='arguments', email='alpha@root.com')
    new_f3_empty = Field("it\'s")
    n1 = Name('Vasyl')
    n2 = Name('Ryan')
    ph1 = Phone('0503453434',
                '099465915',
                '0458465913',
                '380664586953')
    ph2 = Phone('0503453434',
                '0458465913')
    ph_error = Phone('0335005050', name='error')
    ph_email = Phone('user@root.com', name='email')
    ph3 = Phone('0953453434', name='very_strange_and_long_name')
    f3 = Field("it\'s", 'only', 'different', [1, 2], (123, 'others'), ph3)
    r = Record(n1, ph1)
    r2 = Record(n2, ph2)
    r2.add_field(ph_email)

    print('\n{:*^30}\n'.format(' begin '))

    print(f'Record \"{r.name.value}\" ==> {r}')
    a.add_record(r)
    r.add_field(f)
    r.add_field(f2)
    r.add_field(f3)
    print(f'AddressBook with record '
          f'\"{r.name.value}\" ==> {a}')
    print(f'Record \"{r2.name.value}\" '
          f'added field \"{f}\" ==> {r2.add_field(f)}')
    r2.add_field(f2)
    print(f'AddressBook added record '
          f'\"{r2.name.value}\" ==> {a.add_record(r2)}')
    print(f'AddressBook added record '
          f'\"{r2.name.value}\" (repeat) ==> {a.add_record(r2)}')
    print(f'AddressBook: {a}')
    print(f'Edit record \"{r2.name.value}\" '
          f'to \"{new_f2}\" ==> {r2.edit_field(new_f2)}')
    print(f'After edit record \"{r2.name.value}\" '
          f'to \"{new_f2}\" ==> {a}')

    print('\n{:*^30}\n'.format(' first part end '))

    print(f'Delete \"{f2}\" ==>  {r2.delete_field(f2)}')
    print(f'After delete \"{f2}\" ==> {a}')
    print(f'Edit record \"{r.name.value}\" to '
          f'\"{new_f3}\" ==> {r.edit_field(new_f3)}')
    print(f'After edit  record \"{r.name.value}\" '
          f'to \"{new_f3}\" ==> {a}')
    print(f'Delete \"{new_f3_empty}\" '
          f'==> {r.delete_field(new_f3_empty)}')
    print(f'Delete with error in \"{r.name.value}\" '
          f'field \"{ph_error}\" ==> {r.delete_field(ph_error)}')
    print(f'After delete \"{new_f3_empty}\" ==> {a}')

    print('\n{:*^30}\n'.format(' last part end '))


if __name__ == '__main__':
    main()
