first_file = 'Marcel_capitalE_e_la_ViLle.txt'
second_file = 'Kyiv_misto_Stolyzya.ipbn'
third_file = 'Toronto_CITY_CAPital.txt'
fourth_file = 'Berlin_Hauptstadt.txt'
file_names = [first_file, second_file, third_file, fourth_file]
correct_names = []

for name in file_names:

    if name.startswith('Berlin') == True:
        continue

    elif name.endswith('txt') == True:
        correct_names.append(name)

    else:
        continue

print(correct_names)
