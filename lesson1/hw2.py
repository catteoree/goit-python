# a * x ** 2 + b * x + c = 0
a = float(input("Enter value of a: " ))
b = float(input("Enter value of b: " ))
c = float(input("Enter value of c: " ))
d = b ** 2 - 4 * a  *c

if d > 0:

    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

elif d == 0:

    x = -b / (2 * a)
    print(f"For a = {a}, b = {b}, c= {c}, the equation a * x ** 2 + b * x + c = 0 has only one solution: x = {x}.")

else:
    print(f"For a = {a}, b = {b}, c= {c}, the equation a * x ** 2 + b * x + c = 0 has no solutions.")