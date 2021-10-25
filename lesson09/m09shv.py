# carring-01
def hi(name):
    print(f"Hi {name}")


def hello(name):
    print(f"Hello {name}")


FUNCTIONS = {
    'h': hello,
    'r': hi
}


def greating(mod):
    return FUNCTIONS.get(mod, hi)


def main():
    mod = "h"
    hi_function = greating(mod)
    hi_function('Jill')


# old version

# def greating(mod):
#     if mod == "h":
#         return hello
#     else:
#         return hi
#
#
# def main():
#     mod = "r"
#     hello_function = greating(mod)
#     hello_function('Jill')


# cache-02
def outer():
    cache = {}
    def inner_function(y):
        print(cache)
        if y not in cache:
            acumulator = 0
            for i in range(1, y + 1):
                acumulator += i
            cache[y] = acumulator
            print(cache[y])
        return cache[y]
    return inner_function


def main_second():
    inner = outer()
    print(inner(10))
    print(inner(10))


# functional-03
# def func(x):
#     return x % 2


def main_third():
    # for i in map(lambda x: x // 2, [1, 2, 3, 4, 5, 6, 7, 8]):
    #     print(i)

    # for i in filter(func, [1, 2, 3, 4, 5, 6, 7, 8]):
    #     print(i)

    for i in filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8]):
        print(i)


# decorator-04
def log_decorator(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__} called with {args} {kwargs}')
        result = func(*args, **kwargs)
        return result
    return inner


def log_result(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} resulted with {result}')
        return result
    return inner


@log_result
@log_decorator
def sum_(x, y):
    return x + y


def main_fourth():
    sum_(2, 3)
    # print(sum_(20, 7))


if __name__ == "__main__":
    main_fourth()
