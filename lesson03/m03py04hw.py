# 4 nonlocal
# example


    # def func_outer():
    #     x = 2

    #     def func_inner():
    #         nonlocal x
    #         x = 5

    #     func_inner()
    #     return x


    # result = func_outer()  # 5
    # print(result)

# task


    # def discount_price(price, discount):
    #     def apply_discount():
    #         nonlocal price
    #         price -= discount * price

    #     apply_discount()
    #     return price


# 5


    # def get_fullname(first_name="", last_name="", middle_name=""):
    #     if middle_name:
    #         fullname = f"{first_name} {middle_name} {last_name}"
    #     else:
    #         fullname = f"{first_name} {last_name}"
    #     return fullname

# 6


    # def format_string(string, length):
    #     if len(string) < length:
    #         quatity = (length - len(string)) // 2
    #         string = quatity * " " + string
    #     return string


# 7


    # def first(size, *args):
    #     print(size)
    #     print(args)
    #     size += len(args)
    #     return size

    # def second(size, **kwargs):
    #     print(size)
    #     print(len(kwargs))
    #     size += len(kwargs)
    #     return size


# 8

# Только ключевые параметры
# Иногда возникает необходимость, чтобы некоторые ключевые параметры должны быть доступны только по ключу, а не как позиционные аргументы. Для этого их надо объявить после параметра со звёздочкой. Например

# def modeling(factor, *numbers, correction):
#     result = 0
#     for number in numbers:
#         result += number * factor
#     result = result - correction
#     return result


# print(modeling(10, 1, 2, 3, correction=2))  # 58
# Объявление параметра correction после параметра со звёздочкой даёт только ключевые аргументы. Если мы для аргумента не укажем значение по умолчанию или не передадим его при вызове, обращение к функции вызовет ошибку.

# TypeError: modeling() missing 1 required keyword-only argument: 'correction'
# Если нам нужны аргументы, передаваемые только по ключу, но не нужен параметр со звёздочкой, то при объявлении функции можно указать просто звёздочку с подчеркиванием, без указания имени:

# def modeling(factor, *_, correction):
# Задание
# Онлайн-магазин "У Бобра" предоставляет услугу экспресс-доставки для своих товаров
# по цене 5¤ за первый товар в заказе и 2¤ – за все последующие товары. 
# Необходимо реализовать функцию, принимающую в качестве первого параметра количество товаров в заказе quantity,
# так же должен присутствовать параметр, передаваемый только по ключу discount. 
# Параметр discount по умолчанию имеет значение 0 - скидки нет. Принимает значения от 0 до 1. 
# Функция cost_delivery возвращает общую сумму доставки.

# Надо предусмотреть, что функция cost_delivery при вызове может принимать любое количество позиционных аргументов.

# Пример:

# cost_delivery(2, 1, 2, 3)
# При таком вызове quantity равен 2, а параметр discount по умолчанию имеет значение 0

    # def cost_delivery(quantity, *_, discount=0):
    #     if quantity <= 1:
    #         result = 5 * (1 - discount)
    #     else:
    #         result = (1 - discount) * (5 + 2 * (quantity - 1))
    #     return result


# 9


    # def cost_delivery(quantity, *_, discount=0):
    #     """Функция возвращает общую сумму доставки.

    # Первый параметр количество товаров в заказе.
    # Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.
    # """
    #     if quantity <= 1:
    #         result = 5 * (1 - discount)
    #     else:
    #         result = (1 - discount) * (5 + 2 * (quantity - 1))
    #     return result


    # print(cost_delivery.__doc__)


# 10

    # def factorial(n):
    #     if n < 2:
    #         return 1  
    #     else:
    #         return n * factorial(n - 1)    

        
    # def number_of_groups(n, k):
    #     list_quantity = factorial(n) // (factorial(n-k) * factorial(k))
    #     return list_quantity



# 11


def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    # print(factorial(2))
    print(fibonacci(5))