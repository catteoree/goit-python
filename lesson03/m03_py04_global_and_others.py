import string

MY_GLOBAL_VALUE = 50


def global_value():
    global MY_GLOBAL_VALUE
    print(f"(функция) x равно {MY_GLOBAL_VALUE}")
    MY_GLOBAL_VALUE = 2
    print(f"(функция) x равно {MY_GLOBAL_VALUE}")

if __name__ == "__main__":
    print(f"x равно {MY_GLOBAL_VALUE}")

    global_value()
    print(f"x равно {MY_GLOBAL_VALUE}")

    # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/ - ошибки в функциях

    alphabet = string.ascii_letters

    print(alphabet)

    number = int(input("Enter shift number: "))
    source = input("Enter souce text: ")

    result = ""

    for char in source:
        result += alphabet[
            (alphabet.index(char) + number) % len(alphabet)]

print(f"Encrypted: {result}")

