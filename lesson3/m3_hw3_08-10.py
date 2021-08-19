answer1 = ('Spielberg', '30.02.1998', 100, False)
answer2 = ('Lilith', '21.05.1995', 150, True)
answer3 = ('Morbius', '23.01.1999', 200, True)
answer_list = [answer1, answer2, answer3]
surname_list = []

print(answer1[3])

for surname in answer_list:

    if surname[3] == True:
        surname_list.append(surname[0])
    else:
        continue

print(surname_list)

surname_list = []

print(surname_list)

for surname in answer_list:

    for i in surname:

        if i == True:
            surname_list.append(surname[0])
            
print(surname_list)
