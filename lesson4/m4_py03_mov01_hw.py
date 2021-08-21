# generator {1: 5, 2: 4, 3: 0, 4: 2, 5: 1}
print({i: 6-i if i != 3 else 0 for i in range(1, 6)})

d = {i: j for i in range(1, 6) for j in range(5, 0, -1)}
d2 = dict(zip(range(1, 6), range(5, 0, -1)))
print(f"d = {d}\nd2 = {d2}")

# [1, 2, 1, 1, 2, 3, 1, 2, 3]
print([i % 3 + 1 if i != 2 else 1 for i in range(9)])