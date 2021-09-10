sec = int(input("Input seconds: "))

m, s = divmod(sec, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)

print(f"d: {d}, h: {h}, m: {m} and s: {s}.")

# import datetime

# print(datetime.timedelta(seconds=sec))
