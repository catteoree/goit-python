# 01


def read_file(path):
    print(path)
    inf = open(path, "r", encoding="utf-8")
    total_count = 0.0
    try:
        while True:
            line = inf.readline()
            if not line:
                break
            total_count += float(line.split()[1])
            print(line.split()[1])
    except OSError:
        print('Ошибка чтения файла')
    finally:
        inf.close()
    return total_count


# 2


def write_and_get_employees(employee_list, path):
    print(employee_list)
    print(path)
    list_employees = []
    for department in employee_list:
        for employee in department:
            list_employees.append(f"{employee}\n")

    try:
        file = open(path, "w", encoding="utf-8")
        try:
            file.writelines(list_employees)
            print(list_employees)
        except OSError:
            print("Error IO")
        finally:
            file.close()
    except OSError:
        print("Ошибка доступа к файлу")
    try:
        file = open(path, "r", encoding="utf-8")
        try:
            file.read()
        except OSError:
            print("Error IO")
        finally:
            file.close()
    except OSError:
        print("Ошибка доступа к файлу")
    return list_employees


# 3


def add_order(order, path):
    print(order)
    count = 0

    file = open(path, "a")
    try:
        file.write(f"{order}\n")
    except OSError:
        print("Error IO")
    finally:
        file.close()

    file = open(path, "r", encoding="utf-8")
    try:
        string = file.read()
        print(string)
        list_order = string.split("\n")
        print(list_order)
        set_order = set(list_order)
        print(set_order)
        for str_order in set_order:
            if str_order.find(":active") != -1:
                count += 1
    except OSError:
        print("Error IO")
    finally:
        file.close()
    print(count)
    return count


# 4


def navigate_clients(path, code):
    print(code)
    remove_long = len(code) + 1
    print(remove_long)
    file = open(path, "r", encoding="utf-8")
    try:
        file.seek(remove_long)
        first_str = file.readline()
        print(f"First string: {first_str}")
    except OSError:
        print("Error IO")
    finally:
        file.close()
    
    return first_str


# 5


def get_ingredients(path, position_name):
    print(position_name)

    try:

        with open(path, "r", encoding="utf-8") as f:
            string = f.read()
            print(string)
            list_ingredients = string.split("\n")
            print(list_ingredients)

            for ingredients in list_ingredients:
                if ingredients.find != -1:
                    ingredients = ingredients.removeprefix(f"{position_name}:")
                    found_ingredients = ingredients.split(",")

    except OSError:
        print("Ошибка доступа к файлу")

    return found_ingredients


# 6


def encode_password(password):
    print(password)
    list_password_hex = []

    for alpha in password:
        alpha = ord(alpha)
        print(alpha)
        list_password_hex.append(hex(alpha))

    print(list_password_hex)
    return list_password_hex


    # if __name__ == "__main__":
    #     print(encode_password("hardpassword123"))


# 7


def is_equal(utf_8_pass, utf_16_pass):
    if utf_8_pass.decode("utf-8") == utf_16_pass.decode("utf_16"):
        return True
    return False


# 8


def is_equal(utf_8_pass, utf_16_pass):
    if utf_8_pass.decode("utf-8").casefold() == utf_16_pass.decode("utf_16").casefold():
        return True
    return False


# 9


def write_to_bin(path, user_info):
    bin_strings = ""

    for name, pas in user_info.items():
        name = name.encode()
        pas = pas.encode()
        bin_strings += f"{name}:{pas}\n"
    
    print(bin_strings)

    with open(path, 'wb', encoding="utf-8") as bf:
        bf.write(bin_strings)

    with open(path, 'rb', encoding="utf-8") as bf:
        string = bf.read()
        print(string)

        string = string.decode("utf-8")

        list_str_bin = string.split("\n")
        print(list_str_bin)
        for i, value in enumerate(list_str_bin):
            if not value:
                list_str_bin.pop(i)

    return list_str_bin


# 10
    # import shutil


    # def create_archive(path, file_name, employee_residence):
        
    #     for employee, residence in employee_residence.items():
    #         string = f"{employee} {residence}\n"
    #         string = string.encode("utf-8")

    #         with open(f'{path}/{file_name}', "wb") as bf:
    #             bf.write(string)
            
    #     archive = shutil.make_archive('backup', 'zip', path)

    #     return archive


# 11
    # import shutil


    # def unpack(archive_path, path_to_unpack):
    #     shutil.unpack_archive(archive_path, path_to_unpack)

    #     # /folder, /folder1

