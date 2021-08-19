# Create, open, rewrite and read file

    # fh = open('test.txt', 'w+')
    # fh.write('Hello!')
    # fh.seek(0) # cursor on begining

    # first_two_symbols = fh.read(2)
    # print(first_two_symbols)  # 'He'

    # fh.close()

    # fh = open('test.txt', 'w')
    # fh.write('hello!')
    # fh.close()

    # fh = open('test.txt', 'r')
    # while True:
    #     symbol = fh.read(1)
    #     if len(symbol) == 0:
    #         break
    #     print(symbol)

    # fh.close()

# create bytes

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)

for num in numbers:
    print(hex(num))

print(numbers)
print(byte_numbers)
