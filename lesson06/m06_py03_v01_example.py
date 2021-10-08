from pathlib import Path
import os


# cur_path = Path()
# print(cur_path.cwd())

    # py m06_py03_v01_example.py
    # E:\Stu\coder\goit-python\lesson06

# folder_cwd = cur_path.cwd() / "bin" / "utils" / "paint.example.jpg"
# folder = cur_path / "bin" / "utils" / "paint.example.jpg"
# print(folder)
# print(folder_cwd)

    # py m06_py03_v01_example.py
    # E:\Stu\coder\goit-python\lesson06
    # bin\utils\paint.example.jpg

# print(cur_path.joinpath("bin", "utils", "paint.example.jpg"))
# print(folder.parts)
# print(folder.name)
# print(folder.parent)
# print(folder.suffix)
# print(folder.suffixes)

# print(os.name)  # posix nt

# list_dir = Path("lesson06")

# for el in list_dir.iterdir():
#     if el.is_dir():
#         print(f"{el.name} - это директория")
#     if el.is_file():
#         print(f"{el.name} - это файл")

# not_exist = Path('lesson06/m06_py03_v01_head.py')
# print(not_exist.exists())

# *.py **/*.py **/**/*.py

# for el in list_dir.glob("*.py"):
#     print(el)

try:
    tmp = Path("lesson06/test.txt")
    tmp.unlink()
except FileNotFoundError:
    pass

new_dir = Path("lesson06/Test")
if not new_dir.exists():
    new_dir.mkdir()

new_dir = Path("lesson06/Test/temp/asd/baz")
new_dir.mkdir(parents=True, exist_ok=True)
