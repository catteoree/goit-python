from collections import Counter, defaultdict 

# dictionary

    # d = {}
    # d["Hello"] = "World"
    # print(d)

    # d[1] = 2
    # print(d)

    # d["qwerty"] = 5
    # print(d)

    # d[(1, 2)] = 3
    # print(d)

    # d[2] = [1, 2]
    # print(d)

    # d[1] = 5
    # print(d)

    # print(d[1])
    # print(d.get("qwerty", "Error")) # get(key, default)
    # print(d.keys())
    # print(list(d.keys()))
    # print(d.values())
    # print(list(d.values()))

    # print("\n<-----------keys----------->")
    # for i in d.keys():
    #     print(i, end=", ")

    # print("\n\n<----------values---------->")
    # for i in d.values():
    #     print(i, end=", ")

    # print("\n\n<----------items----------->")
    # for key, value in d.items():
    #     print(key, ":", value)

# my

    # d = {1:2, 2:3, 3:2, 4:2}
    # two_in_keys = 0

    # for i in d.keys():
    #     if i == 2:
    #         two_in_keys += 1

    # two_in_values = 0

    # for j in d.values():
    #     if j == 2:
    #         two_in_values += 1
        
    # print(f"2 in keys = {two_in_keys}, 2 in values = {two_in_values}.")

# example 

    # d = {1: 2, 3: 4, 5:2, 2: 6}
    # answer = 0

    # for key, value in d.items():
    #     if key == 2:
    #         answer += 1
    #     elif value == 2:
    #         answer += 1

    # print(answer)

# dictionary count alph in str

# my

# s = input(": ")
# d = {}

    # for char in s:
    #     counter = 0
    #     for i in s:
    #         if char == i:
    #             counter += 1
    #     d[char] = counter

    # print(d)

# example

# print(s.count("h", 1, 5))

# My

    # for char in s:
    #     d[char] = s.count(char)

    # print(d)

# example 1

    # for i in s:
    #     if i in d.keys():
    #         d[i] += 1
    #     else:
    #         d[i] = 1

    # print(d)

# example 2

    # d1 = dict(Counter(s))

    # print(d1)

# example 3

    # d2 = defaultdict(int)
    # for i in s:
    #     d2[i] += 1

    # print(dict(d2))

d = {1: 3, 2: 5}
a = d.pop(1)
print(d, a)
d.clear()
print(d)

d = {1: 3, 2: 5}
a = d
    # for i in d.keys():
    #     if i == 1:
    #         d.pop(1) # RuntimeError: dictionary changed size during iteration

for i in d.copy():
    if i == 1:
        d.pop(1)

print(a)
print(d)

d = [1, 3, 2, 5]
a = d

for i in d.copy():
    if i == 1:
        d.pop(1)

print(a)
print(d)

d = {1: 3, 2: 5, 3: 7}
print(f"<-----------{d}---------->")
print(d.popitem())
a, b = d.popitem()
print(a)
print(b)

d = {1: 3, 2: 5, 3: 7}
d.update({4: 11, 5: 13})
print(d)

keys = [1, 2, 3]
values = [4, 5, 6]

d = {}
for i, key in enumerate(keys):
    d[key] = values[i]

print(d)

d = {"math": 5, "russian": 4, "english": 3, "biology": 4, "ukrainian": 4}
marks = {1:0, 2:0, 3:0, 4:0, 5:0}

# My

for i in d.values():
    if i in marks.keys():
        marks[i] += 1

print(marks)

# example 
# marks = {1:0, 2:0, 3:0, 4:0, 5:0}
marks = {i: 0 for i in range(1, 6)}

for i in d.values():
    marks[i] += 1

print(marks)

# My

answer = 0
numerator = 0
denominator = 0

for i in d.values():
    denominator += 1
    numerator += i

answer = numerator / denominator

print(answer)

# example

print(sum(d.values()) / len(d))

# Max marks
# my 

a = max(d.values())
print(a)

keys = [1, 2, 3, 8, 9]
values = [4, 5, 6, 7]

print(dict(zip(keys, values)))

print(['first line\n', \
    'second line\n', \
    'third line'])


# <------------------------set------------------------->

s = set()
s = {1, 2, 3}
s2 = {1, 4, 5}

l = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]
print(set(l))

print(s & s2)
print(s ^ s2)
print(s | s2)
print(s - s2)
print(s2 - s)

s = {i for i in range(10)}
print(s)