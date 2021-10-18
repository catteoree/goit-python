from datetime import datetime, timedelta
from collections import OrderedDict


def choice_date(not_today=False):
    choiced_date = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

    if not_today:
        choiced_year = int(input("Year YYYY: "))
        choiced_month = int(input("Year MM: "))
        choiced_day = int(input("Year DD: "))

        choiced_date = datetime(year=choiced_year, month=choiced_month, day=choiced_day)

    return choiced_date


choiced_date = choice_date(False)


def calculation_next_week(choiced_date, current_week=False):
    week_day = choiced_date.weekday()

    delta_first = timedelta(days=7 - week_day)
    delta = timedelta(days=6)
    delta_minus = timedelta(days=2)
    if current_week:
        delta_minus = timedelta(days=9)

    first_day = choiced_date + delta_first - delta_minus
    last_day = first_day + delta

    return (choiced_date, first_day, last_day)


def congratulate(users: list):

    monday_list = []
    tuesday_list = []
    wednesday_list = []
    thursday_list = []
    friday_list = []

    for dictionary in users:

        day = dictionary["birthday"]
        name = dictionary["name"]

        week_tuple = calculation_next_week(choiced_date, False)

        new_date = datetime(year=week_tuple[0].year, month=day.month, day=day.day)

        if week_tuple[1] <= new_date <= week_tuple[2]:
            if new_date.weekday() >= 5 or not new_date.weekday():
                monday_list.append(name)
            elif new_date.weekday() == 1:
                tuesday_list.append(name)
            elif new_date.weekday() == 2:
                wednesday_list.append(name)
            elif new_date.weekday() == 3:
                thursday_list.append(name)
            elif new_date.weekday() == 4:
                friday_list.append(name)
            else:
                print("error")

    week_dictionaries = OrderedDict([("Monday", monday_list), ("Tuesday", tuesday_list),
                                     ("Wednesday", wednesday_list), ("Thursday", thursday_list),
                                     ("Friday", friday_list)])

    congratulation_str = ""

    for t in week_dictionaries.items():
        if t[1]:
            congratulation_str += f"{t[0]}: {', '.join(t[1])}\n"

    if not monday_list + tuesday_list + wednesday_list + thursday_list + friday_list:
        congratulation_str = "There are no birthday parties next week"

    return print(congratulation_str)


if __name__ == "__main__":
    users = [{'name': 'Masato', 'birthday': datetime(1972, 10, 16, 0, 0)},
             {'name': 'Veta', 'birthday': datetime(1973, 10, 23, 0, 0)},
             {'name': 'Azamat', 'birthday': datetime(1999, 10, 24, 0, 0)},
             {'name': 'Katsuo', 'birthday': datetime(1997, 10, 25, 0, 0)},
             {'name': 'Dzheremi', 'birthday': datetime(1997, 10, 18, 0, 0)},
             {'name': 'Shamil', 'birthday': datetime(1964, 10, 26, 0, 0)},
             {'name': 'Kondrat', 'birthday': datetime(1940, 10, 22, 0, 0)},
             {'name': 'Avdotia', 'birthday': datetime(1953, 10, 21, 0, 0)},
             {'name': 'Radoslav', 'birthday': datetime(1988, 10, 19, 0, 0)},
             {'name': 'Alena', 'birthday': datetime(1950, 10, 29, 0, 0)}
             ]
    congratulate(users)
