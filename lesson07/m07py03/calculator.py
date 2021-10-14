def calculator(num1: float, num2: float, sign: str):
    
    if sign == "+":
        return num1 + num2

    elif sign == "-":
        return num1 - num2

    elif sign == "**":
        return num1 ** num2

    elif sign == "*":
        return num1 * num2

    elif sign == "/" and num2 != 0:
        return num1 / num2
        
    elif sign == "//" and num2 != 0:
        return num1 // num2

    elif sign == "%" and num2 != 0:
        return num1 % num2
    
    return "error" 


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    c = input("sign: ")
    print(calculator(1, 2, "+"))
    print(calculator(3, 4, "-"))
    print(calculator(5, 6, "**"))
    print(calculator(7, 8, "*"))
    print(calculator(9, 2, "/"))
    print(calculator(12, 0, "//"))
    print(calculator(12, 5, "%"))
    print(calculator(a, b, c))
    print(calculator(int(input("a: ")), int(input("b: ")), input("sign: ")))
