# CTI-110
# P4HW2 - Pizza Order
# Bryan Lee Rivera Lebron 
# 2/27/2022
#

def main():
    tax_rate = 0.06
    keep_going = 'yes'
    num_Students = float(input('How many students do you want to order pizza? '))

    while keep_going.lower() == 'yes':
        num_Share = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
        if num_Share == 1.5 or num_Share == 2 or num_Share == 3:
            num_Pizzas = num_Students / num_Share
            price = num_Pizzas * 5
            tax = price * tax_rate
            total = price + tax

            print('\n----Pizza Order--------')
            print('Number of Students :', num_Students)
            print('Pizzas Needed :', format(num_Pizzas,'.0f'))
            print('price $', format(total,',.2f'), sep='')
            print('--------------------------')

        else:
            print('\nINVALID ENTRY!!!!')
            print('should have entered 1.5, 2 or 3')
            print('\nRun Program again')
            
        keep_going = input("Enter yes to run the program again: ")



main()

# if: How many students do you want to order pizza? = 25
#     Enter number of people per pizza (1.5, 2 or 3): = 4
#     INVALID ENTRY!!!!
#   should have entered 1.5, 2 or 3
#
#   Run Program again
#   Enter yes to run the program again: yes
#
#
#
# if: How many students do you want to order pizza? = 25
#     Enter number of people per pizza (1.5, 2 or 3): = 1.5
#
# Result
#     ----Pizza Order--------
#     Number of Students : 25.0
#     Pizzas Needed : 17
#     price $88.33
#     --------------------------
# Enter yes to run the program again: yes
    

