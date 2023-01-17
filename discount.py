from datetime import datetime

weekday = datetime.today().weekday()

sales_tax_rate = .06
discount_rate = .1
discount = 0
sales_tax = 0

subtotal = float(input('Please enter the subtotal:'))

if subtotal >= 50 and weekday in [1, 2]:
    discount = subtotal * discount_rate
    print(f'Discount amount: {discount:.2f}')
    subtotal -= discount

sales_tax = subtotal * sales_tax_rate
print(f'Sales tax amount: {sales_tax:.2f}')
total = sales_tax + subtotal
print(f'Total: {total:.2f}')

