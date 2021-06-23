surname_to_search = "Spielberg"
surnames_statistic_list = ["Stephen_Spielberg_salary_statistic.xlsx", "Jeff_Mikelson_salary_year.xlsx", "Bosh_Ray_salary.xlsx"]
surnames_income = {"Mikelson": 25000, "Bosh": 16000}
taxes_pay = {"Mikelson", "Bosh"}
not_proper_declaration = []
statistic_flag = False

for statistic in surnames_statistic_list:
    if statistic.find(surname_to_search) != -1:
        statistic_flag = True
    else:
        continue

if statistic_flag == False:
    not_proper_declaration.append("statistic_list")

if surname_to_search not in surnames_income:
    not_proper_declaration.append("income")

if surname_to_search not in taxes_pay:
    not_proper_declaration.append("taxes")

print(not_proper_declaration)