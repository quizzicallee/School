shopping_items = []
item_prices = []
total = 0
action = 0

while action != 5:

    if action == 1:
        add_item = input('What item would you like to add? ')
        capitalized_item = add_item.capitalize()
        shopping_items.append(capitalized_item)
        item_cost = float(input(f'What is the price of {capitalized_item}? '))
        item_prices.append(item_cost)
        print(f'"{capitalized_item}" has been added to the cart')
    elif action == 2:
        for index , shopping_item in enumerate(shopping_items):
            print(f'{index + 1}.{shopping_item} - ${round(item_prices[index], 2)}')
    elif action == 3:
        print('Your list is curreently: ')
        for index , shopping_item in enumerate(shopping_items):
            print(f'{index + 1}.{shopping_item} - ${round(item_prices[index], 2)}')
        try:
            remove = int(input('Which item would you like to remove? '))
            removed_item = shopping_items.pop(remove - 1)
            removed_cost = item_prices.pop(remove - 1)
            print(f'{removed_item} has been removed')
        except IndexError:
            print('Invalid Item please enter a valid item')
        print('Your new list is: ')
        for index , shopping_item in enumerate(shopping_items):
            print(f'{index + 1}.{shopping_item} - ${round(item_prices[index], 2)}')
    elif action == 4:
        for item_price in item_prices:
            total += item_price
            print(f'Your total is {total}')
    elif action > 5 or action < 0 :
        print('Invalid action please try again')
    action = int(input('''Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit
    Please enter an action: '''))
        

