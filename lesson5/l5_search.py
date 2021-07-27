# Парсим url

url = "https://www.google.com/search?q=Cat+and+dog&rlz=1C1GCEA_enUA926UA926&sxsrf=ALeKk03ymyJH0JQamjL3_4M9dakBcz2Tdw%3A1624472432354&ei=cHvTYMKbFe-vrgSu9YygDg&oq=Cat+and+dog&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgIIADIICC4QxwEQrwEyAggAMgIIADIICC4QxwEQrwEyAggAMgIIADIICC4QxwEQrwE6BwgAEEcQsAM6BwgAELADEEM6CgguELADEMgDEEM6EAguEMcBEK8BELADEMgDEENKBQg4EgExSgQIQRgAUK9HWK9HYO9QaAFwAngAgAHOAYgBsgKSAQUwLjEuMZgBAKABAaoBB2d3cy13aXrIAQ3AAQE&sclient=gws-wiz&ved=0ahUKEwjCk5yyr67xAhXvl4sKHa46A-QQ4dUDCA4&uact=5"
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