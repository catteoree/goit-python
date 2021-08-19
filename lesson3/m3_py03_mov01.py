# list

    # l = [1, 3, True, "les"]
    # l += [0, 10, 6]
    # l.insert(3, 2)
    # l.append([4, 2, 5])
    # l.extend([8, 7, 9])

    # print(l)

    # l.remove(2)

    # print(f"After l.remove(2) {l}")

    # l.pop(7)

    # print(f"After l.pop(7) {l}")

    # l *= 3

    # print(f"After l *= 2 {l}")

l = []

# my 

    # for i in range(10):
    #     if not i % 2:
    #         l.append(i)

# example 1

for i in range(2, 11, 2):
    l.append(i)

print(l)

# example 2 <----------------->

l = [i for i in range(2, 11, 2)]
print(l)

# example 3 <----------------->

l = [i*2 for i in range(2, 11, 2)]
print(l)

# example 4 <----------------->

l = [i for i in range(1, 11) if i % 2 == 0]
print(l)

l2 = [i if not i % 2 else 0 for i in range(1, 11)]
print(l2)

# my

l3 = [1 if not i % 2 else 0 for i in range(10)]
print(l3)

# example 

l3 = [0 if i % 2 else 1 for i in range(10)]
print(l3)

# my

l3 = [0 if not i % 2 else 1 for i in range(10)]
print(l3)

# my

l4 = [i for i in range(10, 0, -1)]
print(l4)

s = input(": ")

l5 = [i for i in s if i in "eEyYuUiIoOaA"]
print(l5)

# my 1

l6 = [i for i in s if i in "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"]
print(l6)

# my 2

    # l6 = [i for i in s if i not in "eEyYuUiIoOaA ,/.[];'1234567890"]
    # print(l6)

# my 3

l7 = [i for i in s if i in ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']]
print(l7)

# example 
print("e E y Y u U i I o O a A".split(" "))
l8 = [i for i in s if i in "e E y Y u U i I o O a A".split(" ")]
print(l8)

# MY
l9 = [0]
l9 *= 10 
print(l9)

# EXAMPLE 
l9 = [0] * 10
    # l9[3] = 2
    # l9[4] = 2
l9[3:5] = [2, 2]
print(l9)

s = "abcdefg"
s1 = s[:3] + "aa" + s[5:]
print(f"{s}\n{s1}")

s = list(s)
print(s)

c = (1, 2)
print(c[1])
print(c[0])

c = list(c)
print(c)

c.append(3)
c = tuple(c)
print(c)

c = [[11, 1, 4], 5, 6, 7, 9]
print(len(c))
print(len(c[0]))

c = [[1, 2, 3], [2], [3, 4, 5, 6, 7]]
answer = []

print(len(c), len(c[0]), len(c[1]), len(c[2]))

for i in c:
    print(len(i), end=" ")

    ans = 0

    for j in i:
        ans += j
    
    print(ans)

    answer.append(ans)

print(answer)

# example

# print(sum(c)) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
answer = []

for i in c:
    answer += [sum(i)]

print(answer)

# list with index lists with "3"

# my

answer = []

for i, l in enumerate(c):
    for j in l:
        
        if not j == 3:
            continue

        answer.append(i)

print(answer)

# example 
answer = []

for i, val in enumerate(c):
    
    if 3 in val:
        answer += [i]

print(answer)