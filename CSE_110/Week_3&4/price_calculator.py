#Inputs
kids_meal = input('What is the price of a kids meal? ')
adult_meal = input('What is the price of an adult meal? ')
adult_num = input('How many adults are in your party? ')
kids_num = input('How many kids are in your party? ')
sales_tax = input('What is the sales tax in your area? ')

#Variables for check
kids_meal_check = False
adult_meal_check = False
sales_tax_check = False

#Check for letter in str
for i in kids_meal:
    if i.isalpha():
        kids_meal_check = True
for i in adult_meal:
    if i.isalpha():
        adult_meal_check = True
for i in sales_tax:
    if i.isalpha():
        sales_tax_check = True


#Check for error
if  kids_meal_check == False:
    kids_meal_price = float(kids_meal)
else:
    print('The price of a kids meal has a letter. Please try again and input a number.')
    exit()

if  adult_meal_check == False:
    adult_meal_price = float(adult_meal)
else:
    print('The price of an adult meal has a letter. Please try again and input a number.')
    exit()

if  adult_num.isdigit() == True:
    adult_num_num = int(adult_num)
else:
    print('The number of adults is not an integer. Please try again and input an integer.')
    exit()

if  kids_num.isdigit() == True:
    kids_num_num = int(kids_num)
else:
    print('The number of kids is not an integer. Please try again and input an integer.')
    exit()

if  sales_tax_check == False:
    sales_tax_rate = float(sales_tax)
else:
    print('The sales tax has a letter. Please try again and input a number.')
    exit()


#Calculation
kids_price = kids_meal_price * kids_num_num
adult_price = adult_meal_price * adult_num_num
sales_tax_value = (kids_price + adult_price) * ( sales_tax_rate)
before_tax = kids_price + adult_price
total_price = before_tax + sales_tax_value

#Output With Formatting
print(f'Subtotal: ${round(before_tax, 2)}')
print(f'Sales Tax: ${round(sales_tax_value, 2)}')
print(f'Total: ${round(total_price, 2)}')

#Method of Paying
payment_method = input('Would you like to pay with Cash or Card today? ')

if payment_method == 'Cash' or 'cash':
    payment_amount = float(input('How much cash are you paying with? '))
    if payment_amount > total_price:
        change = payment_amount - total_price
        print(f'Your Change is: ${round(change, 2)}')
    elif payment_amount < total_price:
        remainder = total_price - payment_amount
        print(f'Not enough money you still owe: ${round(remainder, 2)}')
        payment2 = float(input('Please pay the owed in cash: '))
        leave = remainder - payment2
        print(f'im taking the rest as a tip leave.')
    else:
        print('Thank you for shopping with us today have a mint.')
elif payment_method =='Card' or 'card':
    print('Thank you for shopping with us today!')
else:
    print('Payment method not recognized please try again.')
    exit()

