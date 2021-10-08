from pathlib import Path


folder = Path("lesson06/Temp")
list_data = ["Natalia", "Inna", "Andriy", "Ivan"]

try:
    with open(folder / "data.txt", "w", encoding="utf-8") as f:
        for line in list_data:
            f.write(line + "\n")
except OSError:
    print("Ошибка доступа к файлу")
     
try:
    with open(folder / "data_all.txt", "a", encoding="utf-8") as f:
        f.writelines(["Natalia\n", "Inna\n", "Andriy\n", "Ivan"])
except OSError:
    print("Ошибка доступа к файлу")
