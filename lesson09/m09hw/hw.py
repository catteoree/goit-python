def input_error(func):
    try:
        func
    except KeyError:
        print("KeyError")
    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")


@input_error
def handler_hello():
    print("How can I help you?")


def handler_exit():
    print("Good bye!")


@input_error
def handler_add_contact(user_input: str):
    beginning_add = user_input.find("add ")
    print(beginning_add)
    string = user_input[beginning_add + 4:]
    print(string)
    last_i_user = string.find(" ")
    user = string[:last_i_user].capitalize()
    phone = string[last_i_user+1:]
    print(f"User {user} with number {phone} is added successfully.")


def bot():
    while True:
        user_input = input(": ")
        user_input = user_input.casefold()

        if "hello" in user_input:
            handler_hello()
            continue

        if "add" in user_input:
            handler_add_contact(user_input)
            continue

        if "change" in user_input:
            handler_add_contact(user_input)
            continue

        if "phone" in user_input:
            handler_add_contact(user_input)
            continue

        if "show all" in user_input:
            handler_add_contact(user_input)
            continue

        if "good bye" or "exit" or "close" or "." in user_input:
            handler_exit()
            break


if __name__ == "__main__":
    bot()
