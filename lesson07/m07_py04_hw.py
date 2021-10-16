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
# def do_setup(args_dict, requires):
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
# def do_setup(args_dict, requires, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points=entry_points
#           )


# 4
def is_integer(s):
    print(s)
    s = s.strip()

    if not s:
        print(f"s:{s}")
        return False

    if s[0] in "-+":
        s = s[1:]

    if len(s) == 0 or not s.isdigit():
        return False
    else:
        return True


# 5
# import re
#
#
# def capital_text(s):
#     print(s)
#     s_list = []
#
#     while True:
#         sign_search = re.search(r'([.!?])', s)
#         if not sign_search:
#             break
#         print(s)
#         s_list.append(s[:sign_search.start() + 2])
#         s = s[sign_search.start() + 2:]
#
#     s_list.append(s)
#     print(s_list)
#
#     s_capitalize = ""
#
#     for sentence in s_list:
#         s_capitalize += sentence.capitalize()
#
#     print(s_capitalize)
#     return s_capitalize


# 6
def solve_riddle(riddle: str, word_length: int, start_letter: str, reverse=False):
    print(f"{riddle}, {word_length}, {start_letter}, {reverse}")
    print(riddle.find(start_letter))
    if riddle.find(start_letter) != -1:
        # print(riddle[riddle.find(start_letter):riddle.find(start_letter)+word_length])
        if reverse:
            return riddle[riddle.rfind(start_letter):riddle.rfind(start_letter) - word_length:-1]
        else:
            return riddle[riddle.find(start_letter):riddle.find(start_letter) + word_length]


# 7
def data_preparation(list_data):
    print(list_data)
    new_list_data = []
    for list_small in list_data:
        list_small.sort()
        if len(list_small) > 2:
            list_small.pop()
            list_small.pop(0)
        new_list_data += list_small
    new_list_data.sort(reverse=True)
    return new_list_data


# 8
# import re
#
#
# def token_parser(s):
#     print(s)
#     s_list = re.findall(r'\d+|\+|\-|\*|\(|\)', s)
#     print(s_list)
#     return s_list


# 9
def all_sub_lists(data):
    data_len = len(data)
    len_count = data_len
    new_data = []

    while len_count:
        if not data_len-len_count:
            new_data += [[]]
            len_count -= 1
        elif data_len-len_count == 1:
            for i in range(data_len):
                new_data += [[data[i]]]
            len_count -= 1
        else:
            list_len = data_len - len_count
            for i in range(len_count+1):
                new_data += [data[i:i + list_len]]
            len_count -= 1

    new_data += [data]

    return new_data


# 10
def make_request(keys, values):
    print(f"{keys}, {values}")
    request_dict = {}
    if len(keys) != len(values):
        return {}
    for key, value in zip(keys, values):
        request_dict[key] = value

    return request_dict



# 11
def sequence_buttons(string: str):

    ALL_SYMBOLS = "0123456789.,?!: abcdefghijklmnopqrstuvwxyz"
    BUTTONS = "0123456789"
    SYMBOLS = [" ", ".,?!:", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    TRANSFORM_DICT = {}

    string = string.casefold()

    for el in string:
        if el not in ALL_SYMBOLS:
            string = string.replace(el, "")

    for s, b in zip(SYMBOLS, BUTTONS):
        if len(s) == 1:
            TRANSFORM_DICT[ord(s)] = b

        if len(s) == 3:
            TRANSFORM_DICT[ord(s[0])] = b
            TRANSFORM_DICT[ord(s[1])] = b * 2
            TRANSFORM_DICT[ord(s[2])] = b * 3

        if len(s) == 4:
            TRANSFORM_DICT[ord(s[0])] = b
            TRANSFORM_DICT[ord(s[1])] = b * 2
            TRANSFORM_DICT[ord(s[2])] = b * 3
            TRANSFORM_DICT[ord(s[3])] = b * 4

        if len(s) == 5:
            TRANSFORM_DICT[ord(s[0])] = b
            TRANSFORM_DICT[ord(s[1])] = b * 2
            TRANSFORM_DICT[ord(s[2])] = b * 3
            TRANSFORM_DICT[ord(s[3])] = b * 4
            TRANSFORM_DICT[ord(s[4])] = b * 5

    return string.translate(TRANSFORM_DICT)


# 12
def file_operations(path, additional_info, start_pos, count_chars):
    print(f"{path}, {additional_info}, {start_pos}, {count_chars}")

    with open(path, "a") as f:
        f.write(additional_info)

    with open(path, "r") as f:
        f.seek(start_pos)
        string = f.read(count_chars)

    return string


# 13
def get_employees_by_profession(path, profession):
    professions = []

    with open(path, "r") as f:
        employees_list = f.readlines()

    print(employees_list)

    for employee in employees_list:
        print(employee)
        print(employee.find(profession))

        if employee.find(profession) != -1:
            professions.append(employee.replace(profession, "").strip())
            print(professions)

    profession_str = " ".join(professions)

    return profession_str


# 14
def to_indexed(start_file, end_file):
    with open(start_file, "r") as sf:
        sf_list = sf.readlines()

    print(sf_list)

    with open(end_file, "w") as ef:
        for i, el in enumerate(sf_list):
            string = f"{i}: {el}"
            ef.write(string)


# 15
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


# 16
def decode(data):
    if not data:
        return data
    else:
        return list(data[0] * data[1]) + decode(data[2:])


# 17
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
    # print(all_sub_lists([4, 6, 1, 3, 0, 7, 8, 9, 2, 5]))
    # print(all_sub_lists([4, 6, 1, 3, 0]))
    # print(all_sub_lists([4, 6, 1, 3]))
    # [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]

    # "44444084433777331111"
    # import string
    # string.ascii_uppercase
    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.ascii_lowercase
    # 'abcdefghijklmnopqrstuvwxyz'
    # string.ascii_letters
    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(file_operations(['John courier\n', 'Pipe doc\n', 'Dan courier\n']))
