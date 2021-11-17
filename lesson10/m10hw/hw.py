import functools
from collections import UserDict


def sanitize_phone_number(phone: str):
    new_phone = (
        phone.strip()
             .removeprefix('+')
             .removeprefix('3')
             .removeprefix('8')
             .replace('(', '')
             .replace(')', '')
             .replace('-', '')
             .replace(' ', '')
    )
    return new_phone


def is_valid_phone(phone: str):
    def is_valid_operator(phone: str):
        codes_operators = {'039', '067', '068', '096', '097',
                           '098', '050', '066', '095', '099',
                           '063', '093', '091', '092', '094'}
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


class Name:
    def __init__(self, name: str):
        self.value = name

    def __repr__(self):
        return f'{self.value}'


class Field:
    def __init__(self, name, *args, **kwargs):
        if type(name) == Name:
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


class Phone(Field):
    def __init__(self, *args, name='phone'):
        super().__init__(name, *args)
        phones = []

        for phone in self.value:
            phone = sanitize_phone_number(phone)

            if is_valid_phone(phone):
                phones.append(phone)

        if len(phones) == 1:
            self.value = phones[0]
        else:
            self.value = phones


class Record:
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.value = None
        self.data = {}

        print(self.value)
        self.value = {}
        self.value[phone.name] = phone.value
        print(self.value)

        self.data[self.name.value] = self.value

        self.record_name = self.data[self.name.value]

    # def __repr__(self):
    #     return f'{self.name.value}: {self.value}'

    def add_field(self, field: Field):
        if field.name not in self.record_name:
            self.record_name[field.name] = field.value
            return f'Field with name \"{field.name}\" and \"{field.value}\" is added successfully'
        else:
            return 'This field exists.'

    def delete_field(self, field: Field):
        if field.name in self.record_name:
            self.record_name.pop(field.name)
            print(self.record_name)
            return f'Field with name: \"{field.name}\" and value: \"{field.value}\" is deleted successfully'
        else:
            return 'This field not exists.'

    def edit_field(self, field: Field):
        if field.name in self.record_name:
            old_value = self.record_name[field.name]
            self.record_name[field.name] = field.value
            return f'Field with name: \"{field.name}\" and value: \"{old_value}\" changed to \"{field.value}\" successfully'
        else:
            return 'This field not exists.'


class AddressBook(UserDict):
    def add_record(self, record):
        print(f'Begin {[record.name.value], record.value}')
        self.data[record.name.value] = record.value
        print(f'End {self.data[record.name.value]}')
        return f'Record with name: {record.name.value} and value: {record.value} is added successfully'


ADDRESS_BOOK = {}


def input_error(func):
    @functools.wraps(func)
    def wrapped(*args):

        try:
            return func(*args)
        except KeyError:
            print('User name not found. Please try again.')
        except ValueError:
            if args[0] == 'phone':
                """Incorrect response status"""

            elif args[0] == 'change':
                print('Give me user name and new phone please.')

            else:
                print('Give me user name and phone please.')
        except IndexError:
            print('Phone number is not correct or not entered.')

    return wrapped


def search_phone(string: str):
    phone = ''

    for i in string:
        if i.isdigit() or i in '+-() ':
            phone += i
        else:
            break

    return phone


@input_error
def search_contact_info(command: str, user_input: str):
    len_command = len(command) + 1
    user_input_casefold = user_input.casefold()
    first_i_command = user_input_casefold.index(f'{command} ')
    string = user_input[first_i_command + len_command:]
    last_i_user = string.find(' ')

    if command == 'phone':

        if last_i_user == -1:
            return string
        else:
            user = string[:last_i_user]
            return user
    else:
        user = string[:last_i_user]
        phone = search_phone(string[last_i_user + 1:])
        sanitized_phone = sanitize_phone_number(phone)

        if is_valid_phone(sanitized_phone):
            return user, sanitized_phone
        raise IndexError


def handler_hello():
    print('How can I help you?')


def handler_show():
    if not ADDRESS_BOOK:
        print('Records not found.')
    else:
        for user, phone in ADDRESS_BOOK.items():
            print(f'{user}: {phone}')


def handler_add_and_change(command: str, user_input: str):
    info = search_contact_info(command, user_input)
    if not info:
        """Incorrect response status"""
    elif command == 'change' and info[0] in ADDRESS_BOOK:
        phone_old_value = ADDRESS_BOOK[info[0]]
        ADDRESS_BOOK[info[0]] = info[1]
        print(f'Phone {phone_old_value} of user \"{info[0]}\" '
              f'changed to {info[1]} successfully.')
    elif command == 'add':
        ADDRESS_BOOK[info[0]] = info[1]
        print(f'User \"{info[0]}\" with '
              f'phone {info[1]} is added successfully.')
    else:
        print('User name not found. '
              'Maybe you want to enter \"add\"?')


@input_error
def handler_phone(command: str, user_input: str):
    info = search_contact_info(command, user_input)
    print(ADDRESS_BOOK[info])


def handler_exit():
    print('Good bye!')


COMMANDS = {
    'hello': handler_hello,
    'add': handler_add_and_change,
    'change': handler_add_and_change,
    'phone': handler_phone,
    'show all': handler_show,
    'good bye': handler_exit,
    'exit': handler_exit,
    'close': handler_exit,
}


def main():
    command = 'wait'

    while command not in ('good bye', 'exit', 'close'):
        user_input = input(': ')
        user_input_casefold = user_input.casefold()
        no_command = True

        for command in COMMANDS:
            if command in user_input_casefold:
                no_command = False
                command_handler = COMMANDS[command]

                if command in ('add', 'change', 'phone'):
                    command_handler(command, user_input)
                else:
                    command_handler()
                break

        if no_command:
            command = 'wait'
            print("You didn't enter any command. I wait for your commands.")


if __name__ == '__main__':
    # main()
    a = AddressBook()
    f = Field('Ivan', '0501234566')
    f2 = Field('Ivan')
    n1 = Name('Vasyl')
    n2 = Name('Ryan')
    ph1 = Phone('0503453434',
                '099465915',
                '0458465913',
                '380664586953')
    ph2 = Phone('0503453434',
                '0458465913')
    r = Record(n1, ph1)
    r2 = Record(n2, ph2)
    print(f'1: Record {r}')
    a.add_record(r)
    print(f'2: {a}')
    print(f'3: {r2.add_field(f)}')
    print(f'4: {r2.add_field(f2)}')
    a.add_record(r2)
    print(f'5: {a}')
    print(f'6: {r2.edit_field(f2)}')
    print(f'7: {a}')
    print(f'9: {r2.delete_field(f2)}')
    print(f'10: {a}')
