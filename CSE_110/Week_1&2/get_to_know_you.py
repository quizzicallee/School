print('Enter The Following Information: ')
first_name =input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
birth_month = input('Birth Month: ')
training = input('Have you been trained: ')

ID_card = f'''
The ID Card is:
----------------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id_number}

{email_address.lower()}
{phone_number}

Hair: {hair_color.capitalize()}    Eyes: {eye_color.capitalize()}
Month: {birth_month.capitalize()}      Training: {training.capitalize()}
-----------------------------------------------'''

print(f'{ID_card}')