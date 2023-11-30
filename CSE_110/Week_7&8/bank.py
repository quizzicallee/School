account_names = []
account_values = []
account_add = ()
value_add = ()
total_value = 0

print('Enter the names and balances of your bank accounts (type: quit when done)')

while True:
    account_add = input('What is the name of the account? ')
    capitilized_item = account_add.capitalize()
    if account_add != 'quit':
        account_names.append(capitilized_item)
    else:
        break

    value_add = float(input('What is the balance? '))
    account_values.append(value_add)
print('Account Information: ')
for index , account_name in enumerate(account_names):
    print(f'{account_name} - {account_values[index]}')

for account_value in account_values:

    total_value += account_value

average_value = total_value / (len(account_values))

print(f'''Total: ${total_value}
Average: ${average_value}''')