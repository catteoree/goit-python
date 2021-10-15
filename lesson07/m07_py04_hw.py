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
            return riddle[riddle.rfind(start_letter):riddle.rfind(start_letter)-word_length:-1]
        else:
            return riddle[riddle.find(start_letter):riddle.find(start_letter)+word_length]


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
    new_data = []
    len_list = len(data)
    if not data:
        new_data = [[]]
        return new_data
    else:
        for i in range(len_list-1):
            new_data += [data[i]]
        for i in range(len_list-2):
            new_data += data[i:i-len_list]

`
for i in range(len_list):
            new_data += data[i]
        # new_data += [data[0:1-len_list]] + [data[:len_list]] + [data[0:i]] + [data[i:len_list-1]]
        return new_data


if __name__ == "__main__":
    print(all_sub_lists([4, 6, 1, 3])) #[[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]




