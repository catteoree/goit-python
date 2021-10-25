# 1
def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "отлично",
        "B": "очень хорошо",
        "C": "хорошо",
        "D": "удовлетворительно",
        "E": "достаточно",
        "FX": "неудовлетворительно",
        "F": "неудовлетворительно",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None


# 2
DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    print(f"{price}, {customer}")
    if len(customer) > 1:
        price = price * (1 - customer["discount"])
    else:
        price = price * (1 - DEFAULT_DISCOUNT)
    return price


# 3


def caching_fibonacci():
    cache = {}

    def inner(n):
        print(cache)
        if n not in cache:
            fibonacci = lambda n: n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = fibonacci(n)
            print(cache)
        return cache[n]

    return inner


# 4
def discount_price(discount):
    print(discount)

    def inner(price):
        print(price)
        price *= 1 - discount
        return price

    return inner


# 5
def format_phone_number(func):
    def inner(phone):
        if len(func(phone)) == 12:
            preffix = "+"
        else:
            preffix = "+38"
        return preffix + func(phone)
    return inner


@format_phone_number
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


# 6
def generator_numbers(string=""):
    from re import findall
    print(string)

    list_nums = findall(r'\d+', string)
    print(list_nums)

    for num in list_nums:
        num = int(num)
        yield num


def sum_profit(string):
    summ = 0

    for num in generator_numbers(string):
        print(num)
        summ += num
    return summ


# 7
def normal_name(list_name):
    list_normal_name = []

    for i in map(lambda x: x.capitalize(), list_name):
        list_normal_name.append(i)

    print(list_normal_name)
    return list_normal_name


# 8
def get_emails(list_contacts):
    list_emails = []
    for email in map(lambda x: x["email"], list_contacts):
        list_emails.append(email)
    print(list_emails)
    return list_emails


# 9
def positive_values(list_payment):
    print(list_payment)
    list_positive_values = []
    for i in filter(lambda x: x >= 0, list_payment):
        list_positive_values.append(i)
    return list_positive_values


# 10
def get_favorites(contacts):
    print(contacts)
    list_favorites = []
    for i in filter(lambda x: x["favorite"], contacts):
        list_favorites.append(i)
    print(list_favorites)
    return list_favorites


# 11
from functools import reduce


def sum_numbers(numbers):
    summ = reduce(lambda x, y: x + y, numbers, 0)
    return summ


# 12
from functools import reduce


def amount_payment(payment):
    new_payment = []
    for i in filter(lambda j: j > 0, payment):
        new_payment.append(i)
    summ = reduce(lambda x, y: x + y, new_payment, 0)
    return summ


if __name__ == "__main__":
    # cost_15 = discount_price(0.15)
    # cost_10 = discount_price(0.10)
    # cost_05 = discount_price(0.05)
    #
    # price = 100
    # print(cost_15(price))
    # print(cost_10(price))
    # print(cost_05(price))
    # print(sum_profit("The resulting profit was:"
    #                  "from the southern possessions $ 10,"
    #                  "from the northern colonies $50,"
    #                  "and the king gave $100."))
    print(positive_values([100, -3, 400, 35, -100]))
