import re

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911), дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (1860—1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни Рафаэль (1830—1902) из британской еврейской банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году."

pattern = r'\d+'
#result = re.search(pattern, string)

#print(result.span())
#print(result.group())
#print(result.string())

pattern = r'\d+'
result = len(re.findall(pattern, string))
print(result)


result = re.findall(r'[0-9]{4}', string)
print(result)

result = re.findall(r'[А-Я]', string)
print(result)

pattern = r'[А-Я]'
new_pattern = re.compile(string)
print(new_pattern.findall(pattern))

