import math
mass = float(input('What is your mass? '))
gravity = float(input('What is the gravitational constant of the planet you are on(in m/s^2, 9.8 for Earth, 24 for Jupiter)? '))
time = float(input('How long have you been falling? '))
density = float(input('What is the density of the fluid you are falling through(in kg/m^3, 1.3 for air, 1000 for water)? '))
cross_sectional_area = float(input('How much of your body is resisting the air(in m^2)? '))
drag_constant = float(input('What is your drag constant(0.5 for sphere, 1.1 for cylinder)? '))
c = (1/2) * (density * cross_sectional_area * drag_constant)


#speed_of_falling = math.sqrt(mass * gravity / c) * ( 1 - math.e ** -(math.sqrt(mass * gravity * c) / mass * time))
speed_of_falling = math.sqrt(mass * gravity / c) * ( 1 - math.exp (-(math.sqrt(mass * gravity * c) / mass * time)))

print(f'The inner value of c is: {round(c, 3)}')
print(f'Your velocity is: {round(speed_of_falling, 3)}')