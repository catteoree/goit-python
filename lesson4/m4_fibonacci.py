#25th Fibonacсi

def fibonacci(n):
    if n == 0:
        return 0
    elif 0 < n <= 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(9))
    print(fibonacci(25))
