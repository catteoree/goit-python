def say_hello():
    print('Привет, Мир!')   # блок, принадлежащий функции
    # Конец функции say_hello()


# вызов функции
say_hello()

# ещё один вызов функции
say_hello()


def amount_payment(payment):
    payments = 0

    for i in payment:
      if i >= 0 :
          payments += i
      else:
        continue

    return payments


print(amount_payment([200, 300, 400, 700, 20, -200]))


def prepare_data(data):
    new_data = sorted(data)
    print(data)
    print(type(data))
    last = new_data.pop()
    first = new_data.pop(0)
    print(new_data)

    return new_data


def format_ingredients(items):
    if len(items) >= 3:
        last = items[-1]
        new_items = items[0:-1:]
        ingr_string = ', '.join(str(i) for i in new_items) + ' и ' + last
    elif len(items) == 2:
        ingr_string = '' + items[0] + ' и ' + items[1] + ''
    elif len(items) == 0:
        ingr_string = ''
    else:
        ingr_string = '' + items[0] + ''

    return ingr_string


print(format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']))
print(format_ingredients(['яйца 2шт', 'уксус']))        
print(format_ingredients(['сахар 1 л.']))    
print(format_ingredients(['']))    


def get_grade(key):
    dict_ECTS = {'F' : 1, 'FX' : 2, 'E' : 3, 'D' : 3, 'C' : 4, 'B' : 5, 'A' : 5 }
    value = dict_ECTS.get(key)

    return value 



def get_description(key):
    dict_ECTS = {'F' : 'неудовлетворительно', 'FX' : 'неудовлетворительно', 'E' : 'достаточно', 'D' : 'удовлетворительно', 'C' : 'хорошо', 'B' : 'очень хорошо', 'A' : 'отлично' }
    value = dict_ECTS.get(key)

    return value


print(get_grade('A'))
print(get_grade('B'))
print(get_grade('C'))
print(get_grade('D'))
print(get_grade('E'))
print(get_grade('F'))
print(get_grade('FX'))
print(get_grade('c'))

print(get_description('A'))
print(get_description('B'))
print(get_description('C'))
print(get_description('D'))
print(get_description('E'))
print(get_description('F'))
print(get_description('FX'))
print(get_description('c'))


def lookup_key(data, value):
    print(data)
    print(value)
    keys = []

    for key, data_value in data.items():
      if data_value == value:
          keys.append(key)
      else:
          continue

    return keys


def split_list(grade):
    print(grade)
    print(len(grade))
    first_l = []
    second_l = []
    grade_tuple = (first_l, second_l)
    grades = float()

    if len(grade) == 0:
        grade_tuple = ([], [])
    else:
        for i in grade:
            grades += i
            middle = grades / len(grade)

        for j in grade:
            if j <= middle:
                print(type(first_l))
                first = first_l.append(j)
            else:
                second = second_l.append(j)

    return grade_tuple


print(split_list([1, 12, 3, 24, 5]))

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    print(coordinates)
    distance = 0

    if len(coordinates) <= 1:
        return 0
    else:
        print(len(coordinates))

        for i in range(len(coordinates) - 1):
            print(i)
            j = i + 1
            point = [coordinates[i], coordinates[j]]
            new_point = sorted(point)
            print(new_point)
            key = tuple(new_point)
            print(key)
            print(points.get(key, 0))
            distance += points.get(key, 0)
            distance = round(distance, 6)
            print(distance)

        return distance


print(calculate_distance([0, 1, 3, 2, 0, 2]))

user_1 = {"name": "Jane", "age": 21}
user_2 = {"name": "Moris", "age": 23}
user_3 = {"name": "Steve", "age": 24}

persons = [user_1, user_2, user_3]

for user in persons:
    for field in user:
        print(user.get(field))


def game(terra, power):
    print(terra) 
    print(power)
    len_terra = len(terra)
    print(len_terra)

    for i in range(len_terra):
        print(f'i = {i}')

        for j in terra[i]:
            print(f'j = {j}')

            if j <= power:
                power += j
                print(f'power = {power}')
            else:
                break

    return power


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))


def is_valid_pin_codes(pin_codes):
    print(pin_codes)
    nums = set('1234567890')
    print(nums)

    for pin_code in pin_codes:
        if type(pin_code) == type('') and len(pin_codes) == len(set(pin_codes)) and len(pin_code) == 4 and set(pin_code) - nums == set():
            print(pin_code)
            print(len(pin_code))
            print()
            answer = True
        else:
            answer = False
            break
            
    return answer


def is_valid_pin_codes(pin_codes):
    nums = set('1234567890')
    answer = False

    for pin_code in pin_codes:
        print(pin_code)
        print(len(pin_code))
        print(answer)

        if type(pin_code) != type('') or len(pin_codes) != len(set(pin_codes)) or len(pin_code) != 4 or set(pin_code) - nums != set():
            answer = False
            break
        else:
            answer = True

    return answer


print(is_valid_pin_codes(['1101', '9034', '0010']))

from random import randint
