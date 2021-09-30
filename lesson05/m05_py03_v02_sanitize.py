import re

string = "Исключить из этой [строки группы] символов, [расположенные межды] скобками [, ]."

lang = "The best Language Java"
pattern = "Java"

result = re.sub(pattern, "Python", lang)
print(result)

pattern = r"\s\[.*?\]"
result = re.sub(pattern, "", string)
print(result)
