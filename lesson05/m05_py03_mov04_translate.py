str_i = "i i c"
str_ua_i = "і і с"

symbol_map = {ord("і"): "cyrillic i", ord("с"): "cyillic c"}
fixed_string = str_ua_i.translate(symbol_map)

print(ord("і"))
print(fixed_string)
