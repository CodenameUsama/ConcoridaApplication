def main():

# Password Input
    password = input('Please enter password:\n')
    print('--------------------------------------')
    score = 0

# Check Password Length
    if len(password) < 4:
        print('Password must be at least 8 characters.')
    elif 4 < len(password) < 8:
        print('Password must be at least 8 characters.')
        score += 1
    elif len(password) >= 8:
        score += 2

# Check Password Uppercase
    count_upper = 0
    for c in password: 
        if c.isupper():
            count_upper += 1
    if count_upper == 0: 
        print('Password must contain at least 1 uppercase letter.')
    elif count_upper == 1:
        score += 1
    elif count_upper >= 2: 
        score += 2

# Check Password Lowercase
    count_lower = 0
    for c in password: 
        if c.islower():
            count_lower += 1
    if count_lower == 0: 
        print('Password must contain at least 1 lowercase letter.')
    elif count_lower == 1:
        score += 1
    elif count_lower >= 2: 
        score += 2

# Check Password Digits
    count_digit = 0
    for c in password: 
        if c.isdigit():
            count_digit += 1
    if count_digit == 0: 
        print('Password must contain at least 1 digit.')
    elif count_digit == 1:
        score += 1
    elif count_digit >= 2: 
        score += 2

# Check Password Special Character
    special_character = ['!','@','#','$','%','^','&','*','-','_','=','+','/','\\','*','|','(',')','`','~',',','<','>','.','?',';',':','"',"'",'[',']','{','}']
    count_special = 0
    for c in password: 
        if c in special_character:
            count_special += 1
    if count_special == 0: 
        print('Password must contain at least 1 special character.')
    elif count_special == 1:
        score += 1
    elif count_special >= 2: 
        score += 2

# Password Scoring
    print('--------------------------------------')
    if score == 0 :
        print('Password security score: Nonexistent.')
    elif score == 1 or score == 2:
        print('Password security score: Very low.')
    elif score == 3 or score == 4:
        print('Password security score: Low.')
    elif score == 5 or score == 6:
        print('Password security score: Medium.')
    elif score == 7 or score == 8:
        print('Password security score: High.')
    elif score == 9 or score == 10:
        print('Password security score: Very high.')
    else:
        print('Password security score: Error.')

main()

# Multiple Password
while True:
    print('--------------------------------------')
    replay_Q = input('\nWould you like to enter another password?[Y/N]\n')
    if replay_Q == 'Y' or replay_Q == 'y' or replay_Q == 'yes' or replay_Q == 'YES':
        print('--------------------------------------')
        main()
    elif replay_Q == 'N' or replay_Q == 'n' or replay_Q == 'no' or replay_Q == 'NO':
        break
    else:
        print("\n      !Please reply by 'YES' or 'NO', 'Y' or 'N'!")
        continue
    