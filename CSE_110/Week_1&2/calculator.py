use = str(input('Would you like to use a calculator? '))
if use == 'no':
    print('Have a nice day, come again.')
while use == 'yes':
    x = int(input('1st number = '))
    y = int(input('2nd number = '))
    function = input('function: ')
    if function == '+':
        print(x + y)
    elif function == '-':
        print(x - y)
    elif function == '/':
        print(x / y)
    elif function == '*':
        print(x * y)
    else:
        print('function not recognized try again')

    use = input('Do you want to try again? ')
    if use == 'no' or 'No':
        break