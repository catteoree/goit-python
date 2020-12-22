total = 0
user_operator = None
number = 0
# operator_list = ['+', '-', '*', '/', ]

while user_operator != '=':
    
    user_operator = None
    
    while user_operator != '+' and user_operator != '-' and user_operator != '*' and user_operator != '/' and user_operator != '=':
        
        user_operator = input('Enter an operator: ')
        
        if user_operator == '+':
            continue

        elif user_operator == '-':
            continue

        elif user_operator == '*':
            continue

        elif user_operator == '/':
            continue
        
        elif user_operator == '=':
            continue
        
        else:
            print('This is not an operator')

    while user_operator != '=':

        try:
            
            number = input('Enter a number: ')
            numb_f = float(number)
            numb_i = int(numb_f // 1)

            if numb_i != numb_f:
                number = float(number)
            
            else:
                number = int(number)

            if user_operator == '+':
                total += number

            elif user_operator == '-':
                total -= number

            elif user_operator == '*':
                total *= number

            else:
                total /= number
            
        except ValueError:
            print('This is not a number')
            
        else:
            break

print(f'Total: {total}')