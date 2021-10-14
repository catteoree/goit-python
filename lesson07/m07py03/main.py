from print_mode import print_mode
from calculator import calculator
from ...lesson05.m05_py03_v01_count import count_digits


a = int(input("a: "))
b = int(input("b: "))
c = input("sign: ")

answer = calculator(a, b, c)

print(count_digits(print_mode(a, b, c, answer)))