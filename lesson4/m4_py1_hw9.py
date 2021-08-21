# def is_prime(n, d=2):
    
#     if n <= 3:
#         return True
#     elif not n % d:
#         return False
#     elif n <= d:
#         return is_prime(n, 2)
#     elif d == 500:
#         return True

#     return is_prime(n, d + 1) if d * d <= n else False


def is_prime(n, d=3):
    
    if n <= 3:
        return True
    elif not n % d:
        return False
    elif n <= d:
        return is_prime(n, 2)
    elif d == 969:
        return True

    return is_prime(n, d + 1)


print(is_prime(2776))

# def is_prime(n, d=2):
    
#     if d == 20:
#         return True
#     if not n % d:
#         return False
#     return is_prime(n, d + 1) if d * d <= n else False
