floor = 10

quantity_apartments_onefloor = 4

apartment = 267

quantity_apartments_oneentrance = floor * quantity_apartments_onefloor

number_entrance = 1 + (apartment - 1) // quantity_apartments_oneentrance

number_floor = 1 + ((apartment - 1) % quantity_apartments_oneentrance) // quantity_apartments_onefloor

print(f"Number entrance: {number_entrance}, number floor: {number_floor}")