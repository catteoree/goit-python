""" a = 0
while a < 6:
    a = a + 1
    print("Остаток: ", a % 2)
    if a % 2:
        continue
    print(a) """

""" val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway") """

""" def total(a=5, *numbers, **phone_book):
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    #проход по всем элементам словаря
    for first_part, second_part in phone_book.items():
        print(first_part,second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)) """

""" def say_hello(name):
    print(f'Hello {name}')


print("You imported hello.py")
say_hello('user') """

""" def say_hello(name):
    print(f'Hello {name}')



if __name__ == '__main__':
    print("You imported hello.py")
    say_hello('user') """

# def say_hello(name):
#     print(f'Hello {name}')
#
#
#
# def main():
#     print("You imported hello.py")
#     say_hello('user')
#
# def create_recipe():
#     print('Function for recipe creation is implemented')
#
# def change_discount():
#     global discount_count
#     discount_count += 1
#     return discount_count
#
#
# def discount(price, percent_discount):
#     change_discount()
#     price = price
#     if not discount_count % 100:
#         percent_discount = 100
#     price *= (100-percent_discount)/100
#     return price
#
# def add_premium(salary_dict, premium_percent=20):
#
#     for i, val in salary_dict.copy().items():
#         salary_dict[i] = val * (100 + premium_percent) / 100
#
#     return salary_dict
#
#
# if __name__ == '__main__':
#     main()
#     create_recipe()
#
# order_price = 80
# discount_percent = 20
# discount_count = 198
#
# final_price = discount(order_price, discount_percent)
# print(final_price)
# print(final_price)
#
# salary_dict = {"Spielberg": 8000, "Bosh": 1200, "Khamraev": 11000}
# print({i for i in salary_dict.copy()})
# print(add_premium(salary_dict, premium_percent=20))


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m",
               "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh",
               "shch", "ie", "y", "", "e", "iu", "ia", "ie", "i", "i", "g")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.capitalize()

print("оБІВАРПЛД. ЛЩПВІФ РПЄКЖПРЗПРОТФТИЛЮОЙКУЦО АПООФІВРФПЄЖХЙАТИОПРИ Ж.ОМРЯВ".translate(TRANS))