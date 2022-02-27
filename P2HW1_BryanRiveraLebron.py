# This program will calculate the sales tax, subtotal, and total
# 2/26/2022
# CTI-110 P2HW1 - Total Purchases
# Bryan Lee Rivera Lebron
#
    
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0

subtotal = 0.0
sales_tax = 0.0
total = 0.0

# constants
TAX_RATE = .07

# Input
item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

# calculations
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * TAX_RATE
total = subtotal + sales_tax

# display the output
print('\n-------Results-------')
print('Subtotal: ', format(subtotal,'.2f'),sep='')
print("Sales Tax: ", format(sales_tax,'2.2f'),sep='')
print("Total: ", format(total,'2.2f'),sep='')

# If 12.45
# 50.99
# 45
# 90.99
# 96
#   Print response
#       -------Results-------
#       Subtotal: 295.43
#       Sales Tax: 20.68
#       Total: 316.11
