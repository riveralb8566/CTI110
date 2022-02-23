current_price = int(input())
last_months_price = int(input())

''' Type your code here. '''

change  = current_price - last_months_price
new_montage = (current_price * 0.051) / 12

print("This house is $", format(current_price,'.0f'),".", " The change is $", format(change,'.0f')," since last month.",sep='') 
print("The estimated monthly mortgage is $", format(new_montage,'.2f'),".",sep='')
