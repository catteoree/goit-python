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



# 6



# 7



# 8



# 9



# if __name__ == "__main__":
#     print(decimal_average([3, 5, 77, 23, 0.57], 6))
