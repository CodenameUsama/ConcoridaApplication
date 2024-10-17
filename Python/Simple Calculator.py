while True:
    first = float(input('Enter first number: '))
    second = float(input('Enter second number: '))
    operator = input('Enter operator(+, -, *, /): ')

    if operator == '+':
        print(f'{first} + {second} = {first + second}')
    elif operator == '-':
        print(f'{first} - {second} = {first - second}')
    elif operator == '*':
        print(f'{first} x {second} = {first * second}')
    elif operator == '/':
        if second == 0:
            print('Cannot divide by zero')
        else:
            print(f'{first} / {second} = {first / second}')
    else:
        print('Invalid operation. Please choose +, -, * or /')
        continue