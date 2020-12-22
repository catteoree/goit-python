product_count = 20
speed = 5
hours_passed = 0
while product_count >= 0 and speed >= 0:

    print(f'product_count = {product_count}, speed = {speed}, hours_passed = {hours_passed}')
    product_count -= speed
    speed -= 1
    hours_passed += 1
