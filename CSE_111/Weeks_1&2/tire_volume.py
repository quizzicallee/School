import math
from datetime import datetime
def find_volume(width, aspect_ratio, diameter):
    volume = ((math.pi * (width ** 2) * aspect_ratio) * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

#get date
current_date_and_time = datetime.now()

#inputs
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#find volume
volume = find_volume(width, aspect_ratio, diameter)

#append file
with open("volumes.txt", "at") as volume_txt:
    print(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {round(volume, 2)}", file=volume_txt)

#print function
print(f'The approximate volume is {round(volume, 2)} liters')
