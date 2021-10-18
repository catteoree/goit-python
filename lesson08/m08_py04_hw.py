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
# from datetime import date
#
#
# def get_days_in_month(month, year):
#     print(f"{month}, {year}")
#     first_date = date(year, month, 1)
#     try:
#         first_date_next = date(year, month + 1, 1)
#     except ValueError:
#         first_date_next = date(year + 1, month - 11, 1)
#
#     days = first_date_next - first_date
#
#     return days.days

# 3
# from datetime import datetime
#
#
# def get_str_date(date):
#     print(date)
#     date_list = date.split()
#     date = date_list[0]
#     print(date)
#     date = datetime.strptime(date, "%Y-%m-%d")
#     return date.strftime("%A %d %B %Y")


# 4
# from random import randrange
#
#
# def get_numbers_ticket(min, max, quantity):
#     print(f"{min}, {max}, {quantity}")
#
#     list_numbers = []
#
#     if min < 1 or max > 1000 or quantity >= max:
#         return []
#
#
#     for i in range(quantity*quantity):
#         list_numbers.append(randrange(min, max))
#
#     set_numbers = set(list_numbers)
#     list_numbers = list(set_numbers)
#     list_numbers = list_numbers[:quantity]
#
#     list_numbers = sorted(list_numbers)
#
#     return list_numbers


# 5
# import random
#
#
# def get_random_winners(quantity, participants):
#     print(f"{quantity}, {participants}")
#     if quantity > len(participants):
#         return []
#     user_list = list(participants.keys())
#     print(user_list)
#     random.shuffle(user_list)
#     win_list = random.sample(user_list, k=quantity)
#
#     return win_list


# 6
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


# 7



# 8



# 9



# 10



# if __name__ == "__main__":
#     print(get_numbers_ticket(1, 49, 6))
