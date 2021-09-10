# .find()

s = input(": ")

# my .find()

    # index_a = False
    # index = -1

    # for i in s:
    #     index += 1

    #     if i == "a":
    #         index_a = True
    #         break

    # if index_a:
    #     print(index)

    # else:
    #     index = -1
    #     print(index)

# .find() example #1

    # c = 0

    # for i in range(len(s)):
    #     if s[i] == "a":
    #         c = 1
    #         print(i)
    #         break

    # if not c:
    #     print(-1)

# .find() example #2

    # if "a" not in s:
    #     print(-1)

    # else:
    #     for i in range(len(s)):
    #         if s[i] == "a":
    #             print(i)
    #             break

# .find() example #3

    # if "a" not in s:
    #     print(-1)

    # else:
    #     for i, val in enumerate(s):
    #         # if val == "a" or val = "A":
    #         if val in "aA":
    #             print(i)
    #             break

# work out enumerate(x) my style

    # for index, value in enumerate(s):
    #     index = str(index)
    #     print("{" + index + ": "+ value +"}")

# work out enumerate(x) exmple

    # print(dict(enumerate(s))) # enumerate have not yet dictionary

    # for i, val in enumerate(s):
    #     print(f"{i}: {val}")

# rewrite and amount number str

# my variant ~= example, but better

    # amount = 0

    # while amount == 0:

    #     try:

    #         for number in s:
    #             number = int(number)
    #             amount += number
                
    #     except ValueError:
    #         s = input("Number, please: ")

    # print(amount)

# example amount of ints of number

    # n = int(input("Number: "))
    # n = abs(n)
    # answer = 0

    # while n: 
    #     answer += n % 10
    #     n //= 10

    # print(answer)

# rewrite my variant #1

    # n = input("Number: ")
    # long_n = 10**(len(n)-1)
    # n = abs(int(n))
    # answer = 0

    # while n: 
    #     answer += (n % 10) * long_n
    #     n //= 10
    #     long_n //= 10
        
    # print(answer)

# rewrite my variant #2

    # n = int(input("Number: "))
    # n = abs(n)
    # n_quant = n
    # quant = 0
    # answer = 0

    # while n_quant: 
    #     quant += 1
    #     n_quant //= 10

    # print(quant)

    # while n: 
    #     answer += (n % 10) * 10 ** (quant - 1)
    #     n //= 10
    #     quant -= 1
        
    # print(answer)

# rewrite example

    # n = int(input("Number: "))

    # if n > 0:
    #     k = 1
    # else:
    #     k = -1

    # n = abs(n)
    # answer = 0

    # while n: 
    #     answer = answer * 10 + n % 10
    #     n //= 10
        
    # print(k * answer)

# example while  

    # n = 10

    # while n:
    #     print(n)
    #     n -= 1

    # login = "admin"
    # password = "root"
    # ans = 1

    # while ans:

    #     user_l = input("Login: ")
    #     user_p = input("Passwod: ")

    #     if login == user_l and password == user_p:
    #         print(f"Welcome, {login}!")
    #         break

    #     else:
    #         ans = input("Invalid login or password. If you want to continue press 1: ")

    # print("See you next time!")

# example for

    # counter = 0

    # for i in s:

    #     if i in "eEyYuUiIoOaA":
    #         counter += 1

    # for i in s:
        
    #     if i in "1234567890":
    #         counter += 1

    # for i in s:

    #     if i.isdigit():
    #         counter += 1

s = int(s)

counter = 1

    # for num in range(s):
    #     num += 1
    #     if s == 0:
    #         counter = 1
    #     else:
    #         counter *= num

# example 

    # for i in range(1, s+1):
    #     counter *= i

while s:
    counter *= s
    s -= 1

print(counter)
