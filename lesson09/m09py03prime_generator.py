from random import randint


def prime_generator():
    answer = []

    while len(answer) < 10:
        print(answer)
        i = randint(1, 10)
        print(i)
        if i not in answer:
            yield i
            answer.append(i)


def main():
    gen = prime_generator()
    k = 0
    print("-------------------")
    next(gen)
    print("-------------------")
    next(gen)
    print("-------------------")
    for i in gen:
        print(k)
        # print(i)
        k += 1
    print("-------------------")
    next(gen)
    print("-------------------")


if __name__ == "__main__":
    main()
