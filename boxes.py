from math import ceil

number_of_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

number_of_boxes = ceil(number_of_items / items_per_box)

print(f'For {number_of_items} items, packing {items_per_box} in each box, you will need {number_of_boxes} boxes.')
