    # sq = []
    # for i in range(1, 5+1):
    #     sq.append(i**2)

    # print(sq)

# list

numbers = [i for i in range(1, 5+1)]
sq = [i ** 2 for i in range(1, 5+1)]
print(numbers)
print(sq)

# set

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)

# dict

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers}
print(sq)
