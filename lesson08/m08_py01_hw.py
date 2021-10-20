# 1
# from datetime import datetime
#
#
# def get_days_from_today(date):
#     print(date)
#     date = datetime.strptime(date, "%Y-%m-%d")
#     print(date)
#     today = datetime.now()
#
#     days = today - date
#
#     return days.days

# 2
# import random
#
#
# def random_winners(count, user_dict):
#     print(f"{count}, {user_dict}")
#     user_list = list(user_dict.keys())
#     print(user_list)
#     random.shuffle(user_list)
#     win_list = random.sample(user_list, k=count)
#
#     return win_list


# 3
# from decimal import Decimal, getcontext
#
#
# def decimal_average(number_list, signs_count):
#     print(f"{number_list}, {signs_count}")
#
#     getcontext().prec = signs_count
#     number_sum = Decimal(0)
#
#
#     for i in number_list:
#         number_sum += Decimal(i)
#
#     result = number_sum / Decimal(len(number_list))
#
#     return result


# 4
# import math
#
#
# def cil_volume(h, r, x):
#     pi = math.pi
#     x = math.radians(x)
#     v = h * math.sin(x) * pi * r**2
#     return v

# 5
# import collections
#
#
# def to_named(tup):
#     print(tup)
#     discount = ["id", "surname", "discount", "city", "age"]
#     Person = collections.namedtuple("Person", discount)
#     person = Person(*tup)
#
#     return person, person.discount


# 6
# import collections
#
#
# def count_activity(clients_activity):
#     print(clients_activity)
#     general_clients_activities = collections.Counter()
#
#     for activity in clients_activity:
#         general_clients_activities += collections.Counter(activity)
#
#     most_common_client = general_clients_activities.most_common(1)
#
#     return most_common_client


# 7
# from collections import defaultdict
#
#
# def group_clients(clients):
#     print(clients)
#     dict_ids = defaultdict(list)
#
#     for code in clients:
#         un_id = code[:2]
#         dict_ids[un_id].append(code)
#
#     return dict_ids


# 8
from collections import deque


def form_deque(clients_id, max_len):
    print(f"{clients_id}, {max_len}")
    max_len = len(clients_id)
    new_clients_id = deque(clients_id, maxlen=max_len)
    i = 0

    while new_clients_id[0] % 2:
        print(new_clients_id)
        new_clients_id.append(clients_id[i])
        i += 1
        print(new_clients_id)

    return new_clients_id


# 9
def modify_lists(list_for_dict: list, pow_dict: int, list_for_list: list, add_num: int):
    print(f"{list_for_dict}, {pow_dict}, {list_for_list}, {add_num}")
    return {i: i ** pow_dict for i in list_for_dict}, [i + add_num for i in list_for_list]


if __name__ == "__main__":
    # print(to_named((1985, 'Nick', 34.5, 'Kharkiv', 34)))
    # print(group_clients(['34345', '76788', '34654', '76876', '87694']))
    print(modify_lists([12, 3, 4], 3, [4, 3, 5], 10))