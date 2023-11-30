import math
pi = math.pi
shape = input('Which of the three shapes would you like to calculate the area for: Square, Recatngle, or Circle? ').lower()

if shape == 'square':
    side_length_square = float(input('What is the length of the side? '))
    square_area = side_length_square ** 2
    print(f'The area of your square rounded to the thousandths place is: {round(square_area, 3)}')
elif shape == 'rectangle':
    width_rectangle = float(input('What is the width of your rectangle? '))
    length_rectangle = float(input('What is the length of your rectangle? '))
    rectangle_area = width_rectangle * length_rectangle
    print(f'The area of your rectangle rounded to the thousandths place is: {round(rectangle_area, 3)}')
elif shape == 'circle':
    radius_circle = float(input('What is the radius of your cirlce? '))
    area_circle = pi * radius_circle ** 2
    print(f'The area of your circle rounded to the thousandths place is: {round(area_circle, 3)}')
else:
    print('Shape not accepted at the moment please use an accepted shape and try again. ')
    exit()