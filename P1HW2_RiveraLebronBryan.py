# This project helps to see how many pizza and slices you should get in a order of any amount of students.
# 2/14/2022
# CTI-110 P1HW2 - Pizza Order
# Bryan
#

num_Students = int(input('How many students do you want to order pizza?  '))
num_Slides = num_Students * 3
num_Pizzas = num_Students / 2


print('----Pizza Order--------')
print('Number of Students :', num_Students)
print('Pizza Slices Needed:', num_Slides)
print('Pizzas Needed :', num_Pizzas)
print('--------------------------')


# If 5
#   Print response
#       ----Pizza Order--------
#       Number of Students : 5  
#       Pizza Slices Needed: 15
#       Pizzas Needed : 2.5       
#       --------------------------
