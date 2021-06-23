odd_numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2::3]
numbers_copy = numbers[:]

print(odd_numbers, '\n', even_numbers, '\n', three_numbers)

numbers = [0, 1, 2, 3]
first_three = numbers[0:3]
re_numbes = numbers[::-1]
print(first_three, '\n', re_numbes)

products_list = ['Вертел', 'Курица', 'Соус', 'Сыр']
products_copy = products_list[:]
products_reversed = products_list[::-1]
first_and_third_list = products_list[1:4:2]

print(first_and_third_list)

first_string = "Andreev King Larson"
first_list = first_string.split()
second_string = "Swan Ali Guanjo"
second_list = second_string.split()
third_list = first_list.copy()
third_list.extend(second_list)
third_list.sort(reverse=True)

print(third_list)

chars = {'a': 1, 'b': 2}
a = chars.get('c', 1)

print(a)

salary_office_1 = {'Dickens': 15000, 'Bonmarito': 12000, 'Isabalaev': 14000, 'Clinton': 9000}
salary_office_2 = {'Mikelson': 18000, 'Chopin': 20000, 'Kritov': 9000}
salary_office_3 = {'Larson': 9000, 'Kong': 10000}

dickens_salary = salary_office_1['Dickens']
salary_office_3.update({'Dickens': 15000})
salary_office_2_copy = salary_office_2.copy()
salary_office_1.update(salary_office_2_copy)
salary_office_2.clear()
mikelson_salary = salary_office_1['Mikelson']

print(salary_office_1, '\n', salary_office_2, '\n', salary_office_3, '\n', dickens_salary, '\n')

salary_dict = {'Dickens': 15000, 'Bonmarito': 12000, 'Isabalaev': 14000, 'Clinton': 9000}
min_salary = 0
min_salary_key = ""

for min_salary_key, salary in salary_dict.items():
    if salary <= salary_dict['Dickens'] and salary <= salary_dict['Bonmarito'] and salary <= salary_dict['Isabalaev'] and salary <= salary_dict['Clinton']:
        salary_dict[min_salary_key] = int(salary * 124 / 100)
        print(salary_dict['Clinton'])
        min_salary = salary
    else:
        continue


#salary_dict[min_salary_key]