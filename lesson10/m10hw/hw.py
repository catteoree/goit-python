import functools


PHONES_BOOK = {}


def input_error(func):
    @functools.wraps(func)
    def wrapped(*args):

        try:
            return func(*args)
        except KeyError:
            print("User name not found. Please try again.")
        except ValueError:
            if args[0] == "phone":
                pass

            elif args[0] == "change":
                print("Give me user name and new phone please.")

            else:
                print("Give me user name and phone please.")
        except IndexError:
            print("Phone number is not correct or not entered.")

    return wrapped


def search_phone(string):
    phone = ""

    for i in string:
        if i.isdigit() or i in "+-() ":
            phone += i
        else:
            break

    return phone


def sanitize_phone_number(phone):
    new_phone = (
            phone.strip()
            .removeprefix("+38")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


def is_valid_phone(phone: str):
    def is_valid_operator(phone: str):
        codes_operators = {"039", "067", "068", "096", "097", "098", "050", "066",
                           "095", "099", "063", "093", "091", "092", "094"}
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


@input_error
def search_contact_info(command: str, user_input: str):
    len_command = len(command) + 1
    user_input_casefold = user_input.casefold()
    first_i_command = user_input_casefold.index(f"{command} ")
    string = user_input[first_i_command + len_command:]
    last_i_user = string.find(" ")

    if command == "phone":

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
    print(f"How can I help you?")


def handler_show():
    if not PHONES_BOOK:
        print("Records not found.")
    else:
        for user, phone in PHONES_BOOK.items():
            print(f"{user}: {phone}")


def handler_add_and_change(command: str, user_input: str):
    info = search_contact_info(command, user_input)
    if not info:
        pass
    elif command == "change" and info[0] in PHONES_BOOK:
        phone_old_value = PHONES_BOOK[info[0]]
        PHONES_BOOK[info[0]] = info[1]
        print(f"Phone {phone_old_value} of user \"{info[0]}\" changed to {info[1]} successfully.")
    elif command == "add":
        PHONES_BOOK[info[0]] = info[1]
        print(f"User \"{info[0]}\" with phone {info[1]} is added successfully.")
    else:
        print("User name not found. Maybe you want to enter \"add\"?")


@input_error
def handler_phone(command: str, user_input: str):
    info = search_contact_info(command, user_input)
    print(PHONES_BOOK[info])


def handler_exit():
    print("Good bye!")


COMMANDS = {
    "hello": handler_hello,
    "add": handler_add_and_change,
    "change": handler_add_and_change,
    "phone": handler_phone,
    "show all": handler_show,
    "good bye": handler_exit,
    "exit": handler_exit,
    "close": handler_exit
}


def main():
    command = "wait"

    while command not in ("good bye", "exit", "close"):
        user_input = input(": ")
        user_input_casefold = user_input.casefold()
        no_command = True

        for command in COMMANDS:
            if command in user_input_casefold:
                no_command = False
                command_handler = COMMANDS[command]

                if command in ("add", "change", "phone"):
                    command_handler(command, user_input)
                else:
                    command_handler()
                break

        if no_command:
            command = "wait"
            print("You didn\'t enter any command. I wait for your commands.")


if __name__ == "__main__":
    main()
