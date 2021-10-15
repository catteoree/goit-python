# 1
# from setuptools import setup
#
#
# def do_setup(args_dict: dict):
#     print(args_dict)
#     setup(name=args_dict["name"],
#           version=args_dict["version"],
#           description=args_dict["description"],
#           url=args_dict["url"],
#           author=args_dict["author"],
#           author_email=args_dict["author_email"],
#           license=args_dict["license"],
#           packages=args_dict["packages"]
#           )


# 2
# from setuptools import setup
#
#
# def do_setup_2(args_dict, requires):
#     print(f"{args_dict['packages']}")
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires
#           )


# 3
# from setuptools import setup
#
#
# def do_setup_3(args_dict, requiers, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requiers,
#           entry_points=entry_points
#           )


# 4
def file_operations(path, additional_info, start_pos, count_chars):
    print(f"{path}, {additional_info}, {start_pos}, {count_chars}")
    with open(path, "a") as f:
        f.write(additional_info)

    with open(path, "r") as f:
        f.seek(start_pos)
        string = f.read(count_chars)
        return string


# 5
def get_all_couriers(path):
    couriers = []

    with open(path, "r") as f:
        employees_list = f.readlines()

    print(employees_list)

    for employee in employees_list:
        print(employee)
        print(employee.find("courier"))

        if employee.find("courier") != -1:
            couriers.append(employee)
            print(couriers)

    couriers_str = "\n".join(couriers)
    couriers_str = couriers_str.replace("courier", "").strip()

    return couriers_str


# 6
def flatten(data):

    if not data:
        return data

    else:
        print(data)

        if type(data[0]) == list:
            print(data)
            print(flatten(data[0]))

            return flatten(data[0]) + flatten(data[1:])
        else:
            print(data[0])

            return [data[0]] + flatten(data[1:])


# 7
def my_decode(data):
    if not data:
        return ""
    else:
        string = ""
        i = 0

        while i < len(data) - 1:
            if not i % 2:
                string += data[i] * data[i+1]
            i += 1

        return string


def decode(data):
    if not data:
        return data
    else:
        return list(data[0] * data[1]) + decode(data[2:])


def encode(data):
    print(data)
    if not data:
        return []
    else:
        new_data = []
        alpha_count = 0
        new_data += [data[0]]

        while data[0] == data[alpha_count]:
            alpha_count += 1
            if not data[alpha_count:]:
                break

        new_data += [alpha_count]
        return new_data + encode(data[alpha_count:])


if __name__ == "__main__":
    print(encode(['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']))
