def list_sum(l):
    answer = 0
    for i in l:
        answer += i
    return answer

def r_sum(r1):
    r1 += [2]
    return r1


if __name__ == "__main__":
    print(list_sum([1, 2, 4, 5, 7]))
    r = [1, 2, 5, 7, 8]
    print(r_sum(r))
    print(r)
