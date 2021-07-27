from pathlib import Path

p = Path('E:/W/axor')    # p Указывает на папку /home/user/Downloads
for i in p.iterdir():
    print(i.name)   # Выведет в цикле имена всех папок и файлов в /home/user/Downloads
print(p.parent)
print(p.name)
print(Path())