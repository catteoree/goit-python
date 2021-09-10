#25th Fibonacсi

result = 0
first = 1
position = 25

for i in range(0, 26):

    second = result
    result = first + second
    first = second

    print(f'result #{i} = {result}')