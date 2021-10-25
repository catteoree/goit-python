from hw_funcs import make_list_birthday_dictionaries, make_names_list
from datetime import datetime, timedelta


def choice_date(not_today=False):
    choiced_date = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

    if not_today:
        choiced_year = int(input("Year YYYY: "))
        choiced_month = int(input("Year MM: "))
        choiced_day = int(input("Year DD: "))

        choiced_date = datetime(year=choiced_year, month=choiced_month, day=choiced_day)

    return choiced_date


def calculation_next_week(choiced_date, current_week=False):
    week_day = choiced_date.weekday()

    delta_first = timedelta(days=7 - week_day)
    delta = timedelta(days=6)
    delta_minus = timedelta(days=2)
    first_day = choiced_date + delta_first - delta_minus

    if current_week and datetime.now() <= first_day - timedelta(days=7):
        first_day -= timedelta(days=7)

    last_day = first_day + delta

    return choiced_date, first_day, last_day


def congratulate(users: list):
    week_dictionaries = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    for user in users:

        day = user["birthday"]
        name = user["name"]
        week_tuple = calculation_next_week(choiced_date, False)
        new_date = datetime(year=week_tuple[0].year, month=day.month, day=day.day)

        if week_tuple[1] <= new_date <= week_tuple[2]:
            if new_date.weekday() >= 5 or not new_date.weekday():
                week_dictionaries["Monday"] += [name]
            else:
                week_dictionaries[new_date.strftime('%A')] += [name]

    congratulation_str = ""

    for week_day, birth_names in week_dictionaries.items():
        if birth_names:
            congratulation_str += f"{week_day}: {', '.join(birth_names)}\n"

    if not congratulation_str:
        congratulation_str = "There are no birthday parties next week"

    return print(congratulation_str)


if __name__ == "__main__":
    choiced_date = choice_date(False)
    users = make_list_birthday_dictionaries(make_names_list(100), 90, 11)
    for user in users:
        print("|{0[name]:<15}|{0[birthday]}|".format(user))
    congratulate(users)
