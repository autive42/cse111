age = int(input('Enter your age: '))

heart = 220 - age

#print(f'Your max heart rate should be {heart}.')
print(f'When exercising, your heart rate should be in between {int(heart * .65)} and {int(heart * .85)} bpm.')
