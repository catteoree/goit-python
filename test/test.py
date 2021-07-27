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

def say_hello(name):
    print(f'Hello {name}')



def main():
    print("You imported hello.py")
    say_hello('user')

if __name__ == '__main__':
    main()