# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1
#
#
# five_to_ten_generator = interval_generator(5, 10)
#
# print(five_to_ten_generator)
#
# next(five_to_ten_generator) # 5
# next(five_to_ten_generator) # 6
# next(five_to_ten_generator) # 7
# next(five_to_ten_generator) # 8
# next(five_to_ten_generator) # 9
# next(five_to_ten_generator) # 10


# def interval_generator(x, y):
#     print("After First Next Call")
#     yield x
#     print("After Second Next Call")
#     yield x + 1
#     print("After Third next() Call")
#     return None
#
#
# five_to_ten_generator = interval_generator(5, 10)
#
# # print(next(five_to_ten_generator))
# # print(next(five_to_ten_generator))
# # print(next(five_to_ten_generator))
#
# for i in five_to_ten_generator:
#     print(i+2)

def infinit_sequence(start, step, stop):
    while True:
        if start >= stop:
            break
        yield start
        start += step

sequence_generator = infinit_sequence(1, 2, 10)

# for i in sequence_generator:
#     print(i)

# while True:
#     try:
#         print(next(sequence_generator))
#     except StopIteration as si:
#         print(si)
#         break
res = list(sequence_generator)
res_str = sequence_generator.__repr__()
res2 = [i for i in sequence_generator]
print(res)
print(res2)
print(res_str)
