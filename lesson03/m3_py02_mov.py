"""
2 ** 4

2 * 2 ** 3
    2 * 2 ** 2
        2 * 2 ** 1
            2 * 2 ** 0
                1

1 * 2 * 2 * 2 * 2 
"""

def power (x, n):
    """x ** n"""
    if n == 0:
        return 1
    return x * power(x, n - 1)

if __name__ == '__main__':
    print(power(2, 4))
    