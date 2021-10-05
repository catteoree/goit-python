from decimal import Decimal, getcontext


# возвращает настройки точности (prec). Точность: 6 значений после запятой
getcontext().prec = 6

# 1 / 7 = 0.142857
print(Decimal(1) / Decimal(7))

getcontext().prec = 28

# 1 / 7 = 0.142857142857142857429
print(Decimal(1) / Decimal(7))

print(f'0.1 + 0.2 == 0.3 => {0.1 + 0.2 == 0.3} because == {0.1 + 0.2}')

getcontext().prec = 6
print(f'0.1 + 0.2 == 0.3 => {0.1 + 0.2 == 0.3} because == {0.1 + 0.2}')

float(Decimal(0.1) + Decimal(0.2)) == 0.3
print(f'float(Decimal(0.1) + Decimal(0.2)) == 0.3 => {float(Decimal(0.1) + Decimal(0.2)) == 0.3} because float(Decimal(0.1) + Decimal(0.2)) == {float(Decimal(0.1) + Decimal(0.2))} => True')

print(f'Decimal(0.1) + Decimal(0.2) == Decimal(0.3) => {Decimal(0.1) + Decimal(0.2) == Decimal(0.3)} \nbecause Decimal(0.3) == {Decimal(0.3)} => True')

print(f'Decimal(0.1) + Decimal(0.2) == Decimal(0.3) + Decimal(0.0) => {Decimal(0.1) + Decimal(0.2) == Decimal(0.3) + Decimal(0.0)} \nbecause Decimal(0.3) + Decimal(0.0) == {Decimal(0.3) + Decimal(0.0)} => True')
