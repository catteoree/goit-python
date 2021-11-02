# "Enter user name", "Give me name and phone please"

exit_command = False
PHONES_BOOK = {}


def input_error(func):
    def inner(*args):
        print(args)

        try:
            func(*args)
        except KeyError:
            print("Name not found. Please try again")
        except ValueError:
            print("ValueError")  # ???
        except IndexError:
            print("IndexError")  # ???
        else:
            return func(*args)
    
    return inner



def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
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
        if len(phone) == 12 and phone[:2] == "38":
            return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


@input_error
def search_contact_info(command: str, user_input: str):
    len_command = len(command) + 1
    user_input_casefold = user_input.casefold()
    first_i_command = user_input_casefold.find(f"{command} ")
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
        phone = string[last_i_user + 1:]
        sanitized_phone = sanitize_phone_number(phone)

        if is_valid_phone(sanitized_phone):
            return user, sanitized_phone
        else:
            return None


def handler_hello():
    print(f"How can I help you?")


def handler_show():
    for user, phone in PHONES_BOOK.items():
        print(f"{user}: {phone}")


def handler_add_contact(user_input: str):
    contact = search_contact_info("add", user_input)
    PHONES_BOOK[contact[0]] = contact[1]
    print(f"User {contact[0]} with phone {contact[1]} is added successfully.")
    # else:
    #     print("Phone\'s number is not valid. Please try again")


def handler_change(user_input: str):
    contact = search_contact_info("change", user_input)
    print(f"Old value: {PHONES_BOOK[contact[0]]}")
    PHONES_BOOK[contact[0]] = contact[1]
    print(f"User {contact[0]} changed phone to {contact[1]} successfully.")
    # else:
    #     print("Phone\'s number is not valid. Please try again")


def handler_phone(user_input: str):
    contact = search_contact_info("phone", user_input)
    print(PHONES_BOOK[contact])


def handler_exit():
    global exit_command
    print("Good bye!")
    exit_command = True


def bot():
    COMMANDS = {"hello": handler_hello,
                "add": handler_add_contact,
                "change": handler_change,
                "phone": handler_phone,
                "show all": handler_show,
                "good bye": handler_exit,
                "exit": handler_exit,
                "close": handler_exit
                }

    while not exit_command:
        user_input = input(": ")
        user_input_casefold = user_input.casefold()

        for command in COMMANDS:
            if command in user_input_casefold:
                try:
                    COMMANDS[command]()
                except TypeError:
                    COMMANDS[command](user_input)


if __name__ == "__main__":
    bot()
