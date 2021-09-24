from math import factorial


def shift_variations_count(workers_list, shift_count):
    print(workers_list)
    print(shift_count)
    n = len(workers_list)
    variations_count = factorial(n) // (factorial(shift_count) * factorial(n - shift_count))

    return variations_count


def is_prime(n, d=3):
    print(n)
    print(d)
    
    if n <= 3 and n != 1:
        return True
    elif not n % d or n == 1:
        return False
    elif n <= d:
        return is_prime(n, 2)
    elif d == 960:
        return True

    return is_prime(n, d + 1)


if __name__ == "__main__":
    print(is_prime(1))

    workers_list = ['Popii', 'Bosh', 'Mila']
    shift_count = 2
    print(shift_variations_count(['Popii', 'Bosh', 'Mila'], 2))
