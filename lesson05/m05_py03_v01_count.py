def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count


def count_numbers(string):
    count = 0
    position = 0
    while position < len(string):
        if string[position].isdigit():
            number = ""
            while string[position].isdigit():
                number += string[position]
                # print(string[position]
                position += 1
            print(number)
            number = ""
            count +=1
        else:
            position += 1
    return count


if __name__ == "__main__":
    string = "Нильс Бор родился в \
        семье профессора физиологии \
        Копенгагенского университета \
        Христиана Бора (1858—1911), \
        дважды становившегося \
        кандидатом на Нобелевскую \
        премию по физиологии и \
        медицине[10], и Эллен Адлер \
        (1860—1930), \
        дочери влиятельного и весьма \
        состоятельного еврейского \
        банкира и парламентария-\
        либерала Давида Баруха \
        Адлера (дат. David Baruch \
        Adler; 1826—1878) и Дженни \
        Рафаэль (1830—1902) из \
        британской еврейской \
        банкирской династии Raphael \
        Raphael & sons[en][11]. \
        Родители Бора поженились \
        в 1881 году."

    print(f"The quantaty of digits is {count_digits(string)}")
    print(f"The quantaty of numbers is {count_numbers(string)}")
