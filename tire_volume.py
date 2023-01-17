import math
from datetime import datetime

with open("volumes.txt", "at") as volumes_file:

    width = int(input('Enter the width of the tire in mm (ex 205): '))
    ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
    diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    volume = (math.pi * width ** 2 * ratio * (width * ratio + 2540 * diameter))/10_000_000_000

    now = datetime.now()

    print()
    print(f'The approximate volume of the tire is {volume:.2f} liters.')

    print(f'{now:%Y-%m-%d}, {ratio}, {diameter}, {volume:.2f}', file = volumes_file)
