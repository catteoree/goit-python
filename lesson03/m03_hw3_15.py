id_list = [12364, 1535, 112, 1425]
id_income_dict = {12364: 25000, 1535: 16000, 1425: 10000, 112: 14500}
premium_set = set({})

for id_surname in id_list:
    if id_surname % 5 == 0:
        premium_set.add(id_surname)

    else:
        continue

for id_income in id_income_dict:

    if id_income in premium_set:
        id_income_dict[id_income] *= 1.2

    else:
        id_income_dict[id_income] *= 1.15
