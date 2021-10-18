from random import shuffle, randrange
from datetime import datetime, date


def translate_names(string: str):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m",
                   "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh",
                   "shch", "ie", "y", "", "e", "iu", "ia", "ie", "i", "i", "g")

    TRANS = {}

    for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cs)] = trl
        TRANS[ord(cs.upper())] = trl.capitalize()

    return string.translate(TRANS)


def make_names_list(quantity):
    with open("men_names.txt", "r", encoding="utf-8") as men_file:
        string = men_file.read()

    string = translate_names(string)
    men_list = string.split("\n\n")

    with open("men_list.txt", "w", encoding="utf-8") as men_file:
        men_file.write(f"men_list = {men_list}")

    with open("women_names.txt", "r", encoding="utf-8") as women_file:
        string = women_file.read()

    string = translate_names(string)
    women_list = string.split("\n\n")

    with open("women_list.txt", "w", encoding="utf-8") as women_file:
        women_file.write(f"women_list = {women_list}")

    human_list = women_list + men_list
    shuffle(human_list)

    with open("human_list.txt", "w", encoding="utf-8") as human_file:
        human_file.write(f"human_list = {human_list}")

    return human_list[:quantity]


def get_days_in_month(month, year):
    first_date = date(year, month, 1)

    try:
        first_date_next = date(year, month + 1, 1)
    except ValueError:
        first_date_next = date(year + 1, month - 11, 1)

    days = first_date_next - first_date

    return days.days


def random_date(years, month=False):
    today = datetime.now()
    year = randrange(today.year - years, today.year - 18)
    first_day = 1
    if not month:
        month = randrange(1, 12)
    days_in_month = get_days_in_month(month, year)
    max_days = days_in_month

    day = randrange(first_day, max_days + 1)
    search_date = datetime(year=year, month=month, day=day)
    # search_date_format = search_date.strftime("%d %B %Y")

    return search_date


def make_list_birthday_dictionaries(names_list: list, years: int, month=False):
    list_birthday_dictionaries = []
    if not month:
        today = datetime.now()
        month = today.month

    for name in names_list:
        birth_dict = {"name": name, "birthday": random_date(years, month)}
        list_birthday_dictionaries.append(birth_dict)

    return list_birthday_dictionaries


if __name__ == "__main__":
    print(make_list_birthday_dictionaries(make_names_list(100), 90))
