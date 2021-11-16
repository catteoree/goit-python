def sort(l: list):
    print([type(i) for i in l])
    l2 = [i for i in l if isinstance(i, int)]
    return sorted(l2)


print(sort([2, 6, 1, 8, 's', 'b']))

a = 2
b = a if a > 5 else 0

print(b)
