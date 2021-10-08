# 01


from os import name


def total_salary(path):
    print(path)
    inf = open(path, "r", encoding="utf-8")
    total_count = 0.0
    try:
        while True:
            line = inf.readline()
            if not line:
                break
            total_count += float(line.split(",")[1])
            print(line.split(",")[1])
    except OSError:
        print('Ошибка чтения файла')
    finally:
        inf.close()
    return total_count


# 02


def write_employees_to_file(employee_list, path):
    print(employee_list)
    print(path)
    try:
        inf = open(path, "w", encoding="utf-8")
        str_employee = ""
        for department in employee_list:
            for employee in department:
                print(employee)
                str_employee += employee
        
    except OSError:
        print('Ошибка чтения файла')
    finally:
        inf.close()


# 2


def write_employees_to_file(employee_list, path):
    print(employee_list)
    print(path)
    list_employees = []
    for department in employee_list:
        for employee in department:
            list_employees.append(f"{employee}\n")

    try:
        file = open(path, "w")
        try:
            file.writelines(list_employees)
            print(list_employees)
        except OSError:
            print("Error IO")
        finally:
            file.close()
    except OSError:
        print("Ошибка доступа к файлу")

    return list_employees


# 3


def read_employees_from_file(path):
    list_employees = []
    try:
        file = open(path, "r", encoding="utf-8")
        try:
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.rstrip()
                line = line.removesuffix('\n')
                print(f"Начало строки: {line.rstrip()} Конец строки.")
                list_employees.append(line)
        except OSError:
            print("Error IO")
        finally:
            file.close()
    except OSError:
        print("Ошибка доступа к файлу")
    print(list_employees)
    return list_employees


# 4


def add_employee_to_file(record, path):
    print(record)
    try:
        file = open(path, "a")
        try:
            file.write(f"{record}\n")
        except OSError:
            print("Error IO")
        finally:
            file.close()
    except OSError:
        print("Ошибка доступа к файлу")


# 5


def get_cats_info(path):
    found_cats = []

    try:

        with open(path, "r", encoding="utf-8") as f:
            string = f.read()
            list_info = string.split("\n")
            
            for cat in list_info:
                cat_info = cat.split(",")

                cat_dict = {}
                cat_dict["id"] = cat_info[0]
                cat_dict["name"] = cat_info[1]
                cat_dict["age"] = cat_info[2]

                found_cats.append(cat_dict)

    
    except OSError:
        print("Ошибка доступа к файлу")

    print(found_cats)
    return found_cats


# 6


def get_recipe(path, search_id):
    recipe_dict = None

    try:

        with open(path, "r", encoding="utf-8") as f:
            string = f.read()
            list_info = string.split("\n")
            
            for recipe in list_info:
                if recipe.find(search_id) != -1:
                    list_recipe = recipe.split(",")
                    recipe_dict = {}
                    recipe_dict["id"] = list_recipe[0]
                    list_recipe.pop(0)
                    recipe_dict["name"] = list_recipe[0]
                    list_recipe.pop(0)
                    recipe_dict["ingredients"] = list_recipe

    
    except OSError:
        print("Ошибка доступа к файлу")

    print(recipe_dict)
    return recipe_dict


# 7
    # import re


    # def sanitize_file(source, output):
    #     try:

    #         with open(source, "r", encoding="utf-8") as s:
    #             string = s.read()
    #             print(string)
    #             new_string = re.sub(r"\d+", "", string)
    #             print(new_string)

    #     except OSError:
    #         print("Ошибка доступа к файлу")
        
    #     try:

    #         with open(output, "w", encoding="utf-8") as o:
    #             o.write(new_string)

    #     except OSError:
    #         print("Ошибка доступа к файлу")


# 8


def save_applicant_data(source, output):
    print(source)
    list_enrollees = ""

    for dict in source:
        string_enrollee = f"{dict['name']},{dict['specialty']},{dict['math']},{dict['lang']},{dict['eng']}\n"
        list_enrollees += string_enrollee

    print(list_enrollees)

    try:

        with open(output, "w") as f:
            f.write(list_enrollees)

    except OSError:
        print("Ошибка доступа к файлу")
    

# 9


def is_equal_string(utf8_string, utf16_string):
    if utf8_string.decode("utf-8") == utf16_string.decode("utf_16"):
        return True
    return False


# 10


def save_credentials_users(path, users_info):
    print(path)
    print(users_info)

    bin_strings = []

    for name, pas in users_info.items():
        string = f"{name}:{pas}\n"
        bin_strings.append(string.encode("utf-8"))

    print(bin_strings)

    with open(path, 'wb') as bf:
        bf.writelines(bin_strings)


# 11


def get_credentials_users(path):
    list_str_for_bin = []

    with open(path, 'rb') as bf:
        strs_for_bin = bf.read().decode("utf-8")
        list_str_for_bin = strs_for_bin.split("\n")
    
    print(list_str_for_bin)
    return list_str_for_bin


# 