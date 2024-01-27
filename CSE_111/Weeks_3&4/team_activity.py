from datetime import datetime

def main():
    gender = input('What is your Gender?(M or F) ')
    birthday = input('What is your Birthday?(YYYY-MM-DD) ')
    pounds = float(input('What is your weight in U.S. pounds? '))
    inches = float(input('What is your height in U.S. inches? '))

    weight = pounds_to_kilograms(pounds)
    height = inches_to_centimeters(inches)
    age = calculate_age(birthday)
    BMI = calculate_BMI(height, weight)
    if gender == 'M':
        BMR = calculate_BMR_men(weight, height, age)
    elif gender == 'F':
        BMR = calculate_BMR_women(weight, height, age)
    else:
        print('Gender not Recognized try again.')

    print(f'Age (years): {age}')
    print(f'Weight (kg): {round(weight, 2)}')
    print(f'Height (cm): {round(height, 1)}')
    print(f'Body mass index: {round(BMI, 1)}')
    print(f'Basal metabolic rate (kcal/day): {round(BMR, 0)}')

def calculate_BMI(height, weight):
    BMI = (weight * 10000) / (height ** 2)
    return BMI

def calculate_age(birthday):
    birthdate = datetime.strptime(birthday, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def pounds_to_kilograms(weight):
    kg = weight * 0.45359237
    return kg

def inches_to_centimeters(height):
    cm = height * 2.54
    return cm

def calculate_BMR_men(weight, height, age):
    BMR_men = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return BMR_men

def calculate_BMR_women(weight, height, age):
    BMR_women = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return BMR_women

main() 




