login = input(": ")
password = input(": ")

c = 0

with open('input.txt', 'r') as f:
    for line in f:
        parts = line.split(" ")
        print(parts)
        if parts[0] == login and parts[1].strip() == password:
            print("Access")
            c = 1
            break
    if not c:
        print("Wrong")
