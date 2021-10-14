from print_mode import print_mode
from calculator import calculator


a = int(input("a: "))
b = int(input("b: "))
c = input("sign: ")

answer = calculator(a, b, c)

print((print_mode(a, b, c, answer)))
