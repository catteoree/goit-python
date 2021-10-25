AGE = 15


def check(func):
    def inner():
        global AGE
        if AGE >= 18:
            func()
        else:
            print("Deny")
    return inner


@check
def hello_world():
    print("Hello, world!")


if __name__ == "__main__":
    hello_world()
