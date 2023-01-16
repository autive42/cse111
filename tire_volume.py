import math

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * width ** 2 * ratio * (width * ratio + 2540 * diameter))/10_000_000_000

print()
print(f'The approximate volume of the tire is {volume:.2f} liters.')
