# 3/13/2022
# CTI-110 P1HW2 - Pizza Order
# Bryan
#


num_Students = float(input('How many students do you want to order pizza? '))
num_Share = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
tax_rate = 0.06

if num_Share == 1.5 or num_Share == 2 or num_Share == 3:
    num_Pizzas = num_Students / num_Share
    price = num_Pizzas * 5
    tax = price * tax_rate
    total = price + tax

    print('\n----Pizza Order--------')
    print('Number of Students :', num_Students)
    print('Pizzas Needed :', format(num_Pizzas,'.0f'))
    print('price $', total, sep='')
    print('--------------------------')

else:
    print('\nINVALID ENTRY!!!!')
    print('should have entered 1.5, 2 or 3')
    print('\nRun Program again')

# if: How many students do you want to order pizza? = 30
#     Enter number of people per pizza (1.5, 2 or 3): = 2
#
# Result
#     ----Pizza Order--------
#     Number of Students : 30.0
#     Pizzas Needed : 15
#     price $79.5
#     --------------------------
    
