#rider one
age_1 = float(input('How old is the first rider? '))
height_1 = float(input('How tall is the first rider in inches? '))
number_of_riders = input('is there a second rider Y/N? ')

#second rider
if number_of_riders == 'Y':
    age_2 = float(input('How old is the second rider? '))
    height_2 = float(input('How tall is the second rider? '))
#Golden Ticket
golden_ticket = input('Do either riders have a golden ticket?(Y/N) ')
if golden_ticket.upper == 'Y':
    golden_rider = input('Which Rider has the golden ticket the first, second, or both? ')
    if golden_rider.lower() == "first" and 12 < age_1 > 17 :
        age_1 = 18
    elif golden_rider.lower() == "second" and 12 < age_2 > 17 :
        age_2 = 18
    elif golden_rider.lower() == "both" and (12 < age_1 > 17 and 12 < age_2 > 17):
        age_1 = 18
        age_2 = 18
#logic

can_ride = True
if height_1 < 36 or height_2 < 36:
    can_ride = False
elif number_of_riders == 1 and (age_1 < 18 or height_1 < 62):
    can_ride = False
elif number_of_riders == 2 and (age_1 < 18 and age_2 < 18 or ((age_1 < 12 or age_2 < 12) or (height_1 < 52 or height_2 < 52))):
    can_ride = False
    if (age_1 > 16 and age_2 > 14) or (age_1 > 14 and age_2 > 16):
        can_ride = True

#print
if can_ride:
    print("You can ride")
else:
    print("You can't ride")


    