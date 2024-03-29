import re

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета" \
         "Христиана Бора (1858—1911), дважды становившегося кандидатом на Нобелевскую" \
         "премию по физиологии и медицине[10], и Эллен Адлер (1860—1930)," \
         "дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-"\
         "либерала Давида Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни" \
         "Рафаэль (1830—1902) из британской еврейской банкирской династии Raphael" \
         "Raphael & sons[en][11]. Родители Бора поженились в 1881 году."

print(re.findall(r'[^\w]', string))
print(re.findall(r'^\w', string))       # начало слова
print(re.findall(r'^\w+', string))      # первое слово
print(re.findall(r'(\w+)\.?$', string)) # последнее слово /с точкой

pattern = r"[А-Яа-я]{3}\b"
print(re.findall(pattern, string))

pattern = r"\b[А-Яа-я]{3}"
print(re.findall(pattern, string))

pattern = r"\b\d{3}"
print(re.findall(pattern, string))

print(re.findall(r"\d{4}—\d{4}", string))
print(re.findall(r"\d{4}—(\d{4})", string))
print(re.findall(r"(\d{4})—\d{4}", string))
print(re.findall(r"(\d{4})—(\d{4})", string))

result_list = []
iterator = re.finditer(r"\d{4}—(\d{4})", string)
for match in iterator:
    result_list.append(match.group())
print(result_list)
string_findall = '; '.join(result_list)
print(string_findall)

text = "Ima.Fool@iana.org "
print(re.findall(r"@\w+\.\w{2,5}", text))
print(re.findall(r"@\w+\.(\w{2,5})", text))
string_findall = ''.join(re.findall(r"@\w+\.(\w{2,5})", text))
print(string_findall)
