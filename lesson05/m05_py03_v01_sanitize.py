"""
Дана строка символов.
Исключить из этой строки группы символов, 
расположенные между скобками [, ].
Cами скобки тоже должні быть исключены.
Предполагается, что внутри каждой пары скобок нет других скобок.
"""


def sanitize(data):
    new_string = data[:]
    while True:
        start_index = new_string.find(" [")
        end_index = new_string.find("]")
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index+1:]
    return new_string

if __name__ == "__main__":
    string = "Исключить из этой [строки группы] символов, [расположенные межды] скобками [, ]."

    # test = "этой [строки группы] символов"
    # start_index = test.find("[")
    # end_index = test.find("]")
    # print(start_index, end_index)

    # new_string = test[:start_index] + test[end_index + 2:]
    # print(new_string)

print(sanitize(string))
