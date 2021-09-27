# Парсим url

url = "https://www.google.com/search?q=Cat+and+dog&rlz=1C1GCEA_enUA926UA926&oq=Cat+and+dog&aqs=chrome..69i57.1332j0j15&sourceid=chrome&ie=UTF-8"
_, query_search = url.split("?")

print(f"||| query_search = {query_search} |||")

list_parameters = query_search.split("&")

print(f"||| list_parameters = {list_parameters} |||")

object_search = {}
for el in list_parameters:
    key, value = el.split("=")
    object_search.update({key: value.replace("+", " ")})

print(f"||| object_search = {object_search} |||")

url_string = ""

# Формируем строку запроса

for key, value in object_search.items():
    url_string = url_string + "=".join([key, value.replace(" ", "+")])
print(f"||| url_string = {url_string} |||")
