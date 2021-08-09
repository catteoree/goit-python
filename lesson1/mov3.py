# age = int(input("Age: "))
# name = input("Name: ")
# in_years = 45 - age

# print(f"My name is {name}. I am {age} old. My age is 45 in {in_years} years.")

# Calculator

# a = int(input("1: "))
# b = int(input("2: "))
# c = input("Sign: ")

# if c == "/" or c == "//" or c == "%" and b == 0:
#     print("Error")
# elif c == "/":
#     print(a / b)
# elif c == "//":
#     print(a // b)
# elif c == "%":
#     print(a % b)
# elif c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "**":
#     print(a**b)

# range

# for i in range (10, 21, 2):
#     # print(i, i+1, i+2, sep =", ")
#     print(i, end =" ")

# for i in range (11, 21, 2):
#     print(i, end =" ")

# for i in range (11, 21):
#     if not i % 2 == 0:
#         print(i, end =" ")

# for i in range (20, 9, -1):
#     # print(i, i+1, i+2, sep =", ")
#     print(i, end =" ")

# Counter for str

# s = input()
# counter = 0

# print(len(s))

# for i in s:
#     if i != " ": 
#         counter += 1

# print(counter)

# sum = 0

# for i in range(1, 11):
#     sum += i

# print(sum)

# n = int(input("n: "))
# print(n * (n + 1) // 2)

# for str

# s = input("Str: ")
# long_s = len(s)
# answer = ""

# for alpha in range(long_s):
#     print(s[long_s-(alpha+1)], end="")

# for i in range(long_s-1, -1, -2):
#     answer += s[i]
# print(answer)

# for sum int

# n = input("n: ")
# sum = 0

# for i in n:
#     i = int(i)
#     sum += i

# print(sum)

# while

# answer = int(input("1 - print helllo, 2 - print yes, 3 - print no, 0 - print end. \nInput number: "))

# while answer != 0:
#     if answer == 1:
#         print("hello")
        
#     elif answer == 2:
#         print("yes")
        
#     elif answer == 3:
#         print("no")
        
#     answer = int(input("1 - print helllo, 2 - print yes, 3 - print no, 0 - print end. \nInput number: "))
# print("End")


answer = 1

while answer == 1:

    a = int(input("1: "))
    b = int(input("2: "))
    c = input("Sign: ")

    if (c == "/" or c == "//" or c == "%") and b == 0:
        print("Error")
    elif c == "/":
        print(a / b)
    elif c == "//":
        print(a // b)
    elif c == "%":
        print(a % b)
    elif c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "**":
        print(a**b)
    answer = int(input("1 - cotinue: "))

print("End")