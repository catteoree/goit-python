# 2

    # is_admin = input("Пользователь администратор? ")
    # is_active = input("Пользователь активен? ")
    # is_permission = input("Пользователь имеет доступ? ")

    # print(is_admin)
    # print(is_active)
    # print(is_permission)

    # if is_admin == 1:
    #     is_admin = True
    # else:
    #     is_admin = False    
    # if is_active == 1:
    #     is_active = True
    # else:
    #     is_active = False
    # if is_permission == 1:
    #     is_permission = True
    # else:
    #     is_permission = False

    # print(is_active)

    # access = False
        
    # if is_admin:
    #     access = True
    # elif is_active and is_permission:
    #     access = True
    # else:
    #     acess = False

# 3

    # work_experience = int(input("Введите свой стаж полных лет: "))

    # if work_experience > 1 and work_experience <= 5:
    #     developer_type = "Middle"
    # elif work_experience <= 1:
    #     developer_type = "Junior"
    # else:
    #     developer_type = "Senior"

# 4

    # num = int(input("Введите число: "))

    # if num > 0:
    #     if num % 2:
    #         result = "Положительное нечетное число"
    #     else:
    #         result = "Положительное четное число"
    # elif num < 0:
    #     result = "Отрицательное число"
    # else:
    #     result = "Это ноль"

# 8

    # message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
    # search = "r"
    # result = 0

    # for i in message:
    #     if i == search:
    #         result += 1

    # print(result)

# 9

    # first = int(input("Введите первое целое число: "))
    # second = int(input("Введите второе целое число: "))

    # print(first)
    # print(second)

    # nod = first if second > first else second
    # while first % nod or second % nod:
    #     nod -= 1

    # print(nod)

# 10

    # num = int(input("Введите целое число (0 для выхода): "))
    # sum = 0

    # while num != 0:
    #     max_num = int(input("Сумма включительно до? "))
    #     print(max_num)
        
    #     for i in range(max_num+1):
    #         sum += i
    #         print(sum)
            
    #     num = int(input("Введите целое число (0 для выхода): "))

# example 10

    # num = int(input("Введите целое число (0 для выхода): "))
    # sum = 0

    # while num != 0:
        
    #     for i in range(num+1):
    #         sum += i
    #         print(sum)
            
    #     num = int(input("Введите целое число (0 для выхода): "))

# 12

    # sum = 0
    # while True:
    #     num = int(input("Введите целое число (0 для выхода): "))
    #     if num == 0:
    #         break

    #     for i in range(num + 1):
    #         if not i % 2:
    #             sum += i
                
    #     print(sum)

# 13

# Задача: код Цезаря
# Задание
# Довольно часто программисты сталкиваются с задачами кодирования информации. 
# Закодировать сообщение в чате между двумя пользователями. 
# Зашифровать пароль и имя пользователя при аутентификации пользователя по сети и т.д.

# Напишите программу, реализующую код Цезаря. 
# Назван он честь великого римского императора Юлия Цезаря.

# Идея шифрования заключается в циклическом сдвиге букв на заданное количество. 
# Например, если сдвиг на три позиции то, буква A становится буквой D, B – E, и т.д. 
# Последние три буквы алфавита зацикливаются и переносятся в начало. 
# Буква X становится A, Y – B, а Z – C. 
# Цифры, пробелы и другие символы не подвергаются шифрованию.

# В программе пользователь вводит фразу и число для сдвига, 
# после чего надо вычислить новое закодированное сообщение.

# Программа будет шифровать как строчные (a-z), так и прописные буквы (A-Z).

# Для решения этой задачи вам понадобится знание двух новых функций. 
# Первая функция ord. 
# Она преобразует символ в целочисленную позицию в таблице ASCII.

# ord("a")  # 97
# Можно считать, что полученный результат 97 это числовое представление символа a для компьютера.

# Обратная функция chr возвращает строковый символ в таблице ASCII по позиции, переданной в качестве аргумента.

# chr(118)  # 'v'
# Более подробный принцип шифрования.

# Рассмотрим для примера, как зашифровать символ v. 
# Чтобы получить позицию символа v относительно начального символа a необходимо выполнить выражение

# pos = ord('v') - ord('a')  # 21
# Но, согласно алгоритму, нам необходимо учитывать смещение, которое может быть произвольным, например 33. 
# И помнить, что алфавит английского языка основан на латинском алфавите и состоит из 26 букв. 
# Поэтому конечная позиция символа v, относительно символа a, для шифровки с учетом этого равна 2

# pos = ord('v') - ord('a')  # 21
# pos = (pos + 33) % 26  # 2
# Остался последний шаг, получить новый символ:

# pos = ord('v') - ord('a')  # 21
# pos = (pos + 33) % 26  # 2
# new_char = chr(pos + ord("a"))  # 'c'
# Символ v со смещением 33 шифруется символом c

# Hello my little friends!

    # message = input("Введите сообщение: ")
    # offset = int(input("Введите сдвиг: "))
    # encoded_message = ""


    # for ch in message:
    #     if ch in "QWERTYUIOPASDFGHJKLZXCVBNM":
    #         pos = (ord(ch) - ord("A") + offset) % 26
    #         new_ch = chr(pos + ord("A"))
    #         encoded_message += new_ch
    #     elif ch in "qwertyuiopasdfghjklzxcvbnm":
    #         pos = (ord(ch) - ord("a") + offset) % 26
    #         new_ch = chr(pos + ord("a"))
    #         encoded_message += new_ch
    #     else:
    #         encoded_message += ch

    # print(encoded_message)

# 15

result = 0
operand = None
operator = None
wait_for_number = True

operand = int(input("Number: "))
result += operand
wait_for_number = False

while True:
    operator = input("Sign: ")

    if operator == "=":
        print(result)
        break

    while operator not in "+-*/=":
        print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
        operator = input("Sign: ")
    
    wait_for_number = True
    
    while wait_for_number:
        try:
            operand = input("Number: ")
            operand = int(operand)
        except ValueError:
            print(f"{operand} is not a number. Try again")
        else:
            wait_for_number = False

    if operand == 0 and operator == "/":
        print("You cannot divide by zero. Try again")

    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/" and operand != 0:
        if result % operand:
            result /= operand
        else:
            result //= operand

