red_amount = int(input())
green_amount = int(input())
blue_amount = int(input())

min_value = red_amount

if green_amount < min_value:
    min_value = green_amount
if blue_amount < min_value:
    min_value = blue_amount
# remove gray
red_amount = red_amount - min_value
green_amount = green_amount - min_value
blue_amount = blue_amount - min_value

#
print(red_amount, green_amount, blue_amount)
