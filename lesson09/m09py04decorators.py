import functools


# def call_4_times(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = 0
#         for _ in range(4):
#             value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
#
#
# @call_4_times
# def hello(word):
#     print(f"Hello {word}")
#     return len(word)


def call_n_times(n):
    def decorator_factory(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            print("Wrapper started working")
            # Do something before
            value = 0
            for _ in range(n):
                value = func(*args, **kwargs)
            # Do something after
            print("Wrapper finished working")
            return value
        return wrapper_decorator
    return decorator_factory


@call_n_times(7)
def _hello(word):
    print(f"Hello {word}")
    return len(word)


def makeupper(fn):
    def wrapped(val):
        res = "<u>" + fn(val.upper()) + "</u>"
        print(f"Makeupper: {fn}, {val}")
        return res

    return wrapped


def makebold(fn):
    def wrapped(val):
        res = "<b>" + fn(val) + "</b>"
        print(f"Makebold: {fn}, {val}")
        return res

    return wrapped


def makeitalic(fn):
    def wrapped(val):
        res = "<i>" + fn(val) + "</i>"
        print(f"Makeitalic: {fn}, {val}")
        return res

    return wrapped


@makeupper
@makebold
@makeitalic
def hello(val):     # hello = makeupper(makebold(makeitalic(hello)))
    return val


if __name__ == "__main__":
    # hello = makeupper(makebold(makeitalic(hello)))
    # print(_hello("Kostia"))
    print(hello("go it"))



