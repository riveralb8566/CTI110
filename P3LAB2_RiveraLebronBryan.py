# Type your code here

auto_service = str(input('Enter desired auto service:'))
print('\nYou entered:', auto_service,)

if auto_service ==  "Oil change" :
    print('Cost of oil change: $35') 
   
elif auto_service == "Tire rotation":
    print('Cost of tire rotation: $19')

elif auto_service == "Car wash":
    print('Cost of car wash: $7')

else:
    print('Error: Requested service is not recognized')
    



