"""
Есть список телефонов. Санитизировать. 

"""

phone_storage = ["38(050)123 45 67", "+38(050)123-67-82", "380391431534", "380634213431", "3243489532", "380391452134", "38066435325423"]

"""
+380501234567 + 38 code country 050 code operator tel: 1234567

"""

codes_operators = {"039", "050", "063", "067", "095", "066"}

def is_valid_phone(phone):
    def is_valid_operator(phone):
        if phone[:3] in codes_operators:
            return True
        return False

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
                .replace("-", ""))
    return new_phone

for phone in phone_storage:
    phone = sanitize_phone(phone)
    is_valid = is_valid_phone(phone)
    if is_valid:
        print("Телефон {:>12} валиден".format(phone))
    else:
        print("Телефон {:>12} не валиден".format(phone))

def pretty_table():
    print("|{:^14}|{:^12}|".format("Телефон", "Результат"))
    print("|{:^14}|{:^12}|".format("-" * 14, "-" * 12))
    for phone in phone_storage:

