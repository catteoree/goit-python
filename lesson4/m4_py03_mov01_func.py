def rewrite_list():
    global l
    a = len(l)
    l2 = []

    while a:
        a -= 1
        l2.append(l.pop())

    l = l2
    return l

def rewrite_list_example1(l: list):
    # global l
    l.reverse()

    return l

def rewrite_list_example2():
    global l
    l = l[::-1]

    return l

def str_counter(s):
    d = {}
    
    for char in s:
        d[char] = s.count(char)

    return d


if __name__ == "__main__":
    l = [i for i in range(0, 21, 2)]
    s = input(": ")
    print(l)
    print(rewrite_list())
    print(rewrite_list_example1(l))
    print(rewrite_list_example1(l))
    print(rewrite_list_example2())
    print(rewrite_list_example2())
    print(str_counter(s))
    