first_name = str(input('Hello, What is your first name? '))
last_name = str(input(f'What is your last name {first_name}? '))
check = str(input(f'{last_name}, {first_name} {last_name}? are you sure?.'))
if check == "yes" or "Yes":
    print('Then today you die.')
else:
    print('Then leave this place at once.')