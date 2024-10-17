import math
from datetime import datetime
from datetime import date
from datetime import timedelta

now = datetime.now()

#user input
while True: 
    operation = input('chose operator (+, - or <) : \n')
    if operation == '+' or operation == '-':
        var = int(input('chose a number of days : \n'))
    elif operation =='<':
        varSTR =(input('chose a date you want to compare to (YYYY-MM-DD): \n'))
        year, month, day = map(int, varSTR.split('-'))
        if month > 12 or day > 31:
            print('Invalid date format. Please enter a date in the format YYYY-MM-DD.')
            continue
        var = datetime(year, month, day)
    else: 
        print('Please chose a valid operator (+, - or <)')
        continue

#calculator
    if operation == '+':
        print(f'in {var} days, the date will be {now + timedelta(var)}\n\n')
    elif operation == '-':
        print(f'{var} days ago was {now - timedelta(var)}\n\n')
    if operation == '<':
        if now < var:
            print('\n', var, 'is after', now, '\n\n')
        else:
            print('\n', var, 'is before', now, '\n\n')



