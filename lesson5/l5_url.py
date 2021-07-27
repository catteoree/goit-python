url_rozetka = "https://rozetka.com.ua/mobile-phones/c80003/osobennosti-osnovnoy-kamery=shirokougolniy-obektiv;producer=xiaomi;20850=ot-25-mp-do-47-mp;23777=6-6-5/"

query_url_rozetka = "osobennosti-osnovnoy-kamery=shirokougolniy-obektiv;producer=xiaomi;20850=ot-25-mp-do-47-mp;23777=6-6-5/"

query_rozetka = query_url_rozetka.split(";")

print(query_rozetka)

object_rozetka = {}
for el in query_rozetka:
    key, value = el.split("=")
    object_rozetka.update({key: value})

print(object_rozetka)