"""
Есть список телефонов. Убрать все ошибочніе строки и привести всех  одинаковому виду. 
[" 380669640547", " 0637306465 ", "380961935171 ", \
"  632643973", "508325200", "000000000", \
" 48730283918 ", "986223575", "375297947963", \
" 38 (050) 123 45 67 ", "+38(050)123-67-82", \
"380391431534", "380634213431", "3243489532", \
" 38039145 21 34 ", " 38066435325423 ", " 380009640547 ", " 38050xxxxxxx"]
"""

"""
+380501234567 + 38 code country 050 code operator tel: 1234567
"""


def _is_valid_phone(phone):
    codes_operators = {"039", "067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "093", "091", "092", "094"}
    if len(phone) == 12:
        if phone[:2] == "38":
            if phone[2:5] in codes_operators:
                return True
            else:
                return False
        else:
            return False
    if len(phone) == 10:
        if phone[:3] in codes_operators:
            return True
        else:
            return False
    return False


def is_valid_phone(phone):
    def is_valid_operator(phone):
        codes_operators = {"039", "067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "093", "091", "092", "094"}
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == "38":
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                .removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace(" ", "")
                .replace("-", "")
                )
    return new_phone


def pretty_table():
    print("|{:^14}|{:^12}|".format("Телефон", "Результат"))
    print("|{:^14}|{:^12}|".format("-" * 14, "-" * 12))
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("|{:^14}|{:^12}|".format(phone, "валиден"))
        else:
            print("|{:^14}|{:^12}|".format(phone, "не валиден"))


if __name__ == "__main__":
    
    phone_storage = [" 380669640547", " 0637306465 ", "380961935171 ", \
    "  632643973", "508325200", "000000000", \
    " 48730283918 ", "986223575", "375297947963", \
    " 38 (050) 123 45 67 ", "+38(050)123-67-82", \
    "380391431534 ", " 380634213431", "3243489532", \
    " 38039145 21 34 ", " 38066435325423 ", " 380009640547 ", " 38050xxxxxxx"]

    pretty_table()
