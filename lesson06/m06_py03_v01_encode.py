from pathlib import Path


message =  "Привет мир!"

print(message.encode())
print(message.encode("utf_16"))
print(message.encode("cp1251"))

print(b"\xec\xe8\xf0!".decode("cp1251"))


folder = Path("lesson06/Test")

with open(folder / "utf-8.txt", "wb") as f:
    f.write(message.encode())
with open(folder / "utf-16.txt", "wb") as f:
    f.write(message.encode("utf_16"))
with open(folder / "cp1251.txt", "wb") as f:
    f.write(message.encode("cp1251"))

with open(folder / "utf-8.txt", "rb") as f:
    print(f.read().decode("utf-8"))
with open(folder / "utf-16.txt", "rb") as f:
    print(f.read().decode("utf_16"))
with open(folder / "cp1251.txt", "rb") as f:
    print(f.read().decode("cp1251"))
    # print(f.read())
