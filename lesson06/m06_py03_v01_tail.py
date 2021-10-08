import sys


NUM_LINES = 18

if len(sys.argv) != 2:
    print('Не передано имя файла для прочтения')
    quit()

try:
    with open(sys.argv[1], "r", encoding="utf-8") as inf:
        lines = []
        for line in inf:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        for line in lines:
            print(line, end="")
except OSError:
    print('Ошибка доступа к файлу')

# cd lesson06
# py m06_py03_v01_tail.py m06_py03_v01_tail.py

