# 1
def form_client(id, info):
    print(f"{id}, {info}")
    return {id: info}


def form_employee(id, info):
    print(f"{id}, {info}")
    return id, info


def choose_mode(mode, id, information):
    print(f"{mode}, {id}, {information}")
    if mode == 'client':
        return form_client(id, information)
    elif mode == 'employee':
        return form_employee(id, information)
    else:
        return None


# 2
DEFAULT_DISCOUNT = 5


def discount(id, price, discount_percent):
    print(f"{id}, {price}, {discount_percent}")
    if not id % 5:
        return price * (100 - discount_percent) / 100
    else:
        return price * (100 - DEFAULT_DISCOUNT) / 100


# 3
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def caching():
#     cache = {}
#
#     def inner(n):
#         if n not in cache:
#             cache[n] = fibonacci(n)
#             print(fibonacci)
#             print(cache)
#         return cache[n]
#     return inner


# def caching():
#     cache = {}
#
#     def inner(n):
#         print(cache)
#         if n not in cache:
#             fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
#             cache[n] = fibonacci(n)
#             print(cache)
#         return cache[n]
#     return inner


# 4
def discount_carr(discount):
    def real_cost(cost):
        cost *= 1 - discount
        return cost

    return real_cost


# 5
# from math import sqrt
#
#
# def function_root(func):
#
#     def inner(x, y, z):
#         return sqrt(func(x, y, z))
#
#     return inner
#
#
# @function_root
# def complicated(x, y, z):
#     return x ** 2 + y ** 2 + z ** 2


# 6
def generator_string(str=""):
    print(str)
    list_nums = []
    for num in str:
        print(num)
        if num.isdigit():
            num = int(num)
            yield num
            list_nums.append(num)


def sum(str):
    summ = 0

    for num in generator_string(str):
        print(num)
        summ += num
    return summ


# 7
encode_lambda = lambda x: x ** 0.5


# 8
def to_root(number_list, selected_pow, number):
    new_number_list = []
    for i in map(lambda x: x ** selected_pow + number, number_list):
        print(i)
        new_number_list.append(i)
    return new_number_list


# 9
def filter_letters(surnames_list):
    new_surnames_list = []
    print(surnames_list)
    for name in surnames_list:
        for alpha in filter(lambda x: x.isnumeric(), name):
            name = name.replace(alpha, "")
        new_surnames_list.append(name)

    return new_surnames_list


if __name__ == "__main__":
    # inner = caching()
    # print(inner(0))
    # print(inner(1))
    # print(inner(2))
    # print(inner(3))
    # print(inner(4))
    # print(inner(5))
    # print(inner(6))
    # print(inner(7))
    # print(inner(8))
    # print(inner(10))
    # print(inner(11))
    # print(inner(12))
    print(filter_letters(['Po3livanov1','3Bos6ton','3Mali5vtse4v']))
