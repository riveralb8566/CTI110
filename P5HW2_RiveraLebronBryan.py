# This project should make simple math questions
# 4/14/2022
# CTI-110 P5HW2 - Math Quiz
# Bryan Lee Rivera Lebron 
#

print('Welcome to the Math Quiz')
print()
print()
def menu():
    keep_going = "y"
    while (keep_going.lower()=="y"):
        choices_list = [1,2,3] 
        count = 0
        print("MAIN MENU")
        print("--------------------")
        print("  1. Adding Random Numbers")
        print("  2. Subtracting Random Numbers")
        print("  3. Exit")
        choice = int(input("Please enter one of the menu options: "))
        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            keep_going = 'n'
        else:
            print("Try again choice 1, 2, or 3")
            choice = int(input("Please enter one of the menu options: "))
           
            
def add():
    count = 1
    import random

    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    results = num1 + num2
    
    print(num1)
    print("+", num2)

    tested = int(input('Enter answer: '))


    while tested != results:

        if tested <= results:
            count = count + 1
            tested = int(input('Too low, try again and enter number: '))

        else:
            count = count + 1
            print("try again, too high")
            tested = int(input('Enter answer: '))


    if tested == results:

        if count == 1:
            print('WOW')
            print("!!!You have DONE it in in your FIRST try, GOOD JOB!!!")

        elif count != 1:
            print("You have DONE it in this amount of tries", count ,"GOOD JOB")


        
def subtract():
    count = 1
    import random

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    results = num1 - num2
    
    print(num1)
    print("-", num2)

    tested = int(input('Enter answer: '))


    while tested != results:

        if tested <= results:
            count = count + 1
            tested = int(input('Too low, try again and enter number: '))


        else:
            count = count + 1
            print("try again, too high")
            tested = int(input('Enter answer: '))


    if tested == results:
        if count == 1:
            print('WOW')
            print("!!!You have DONE it in in your FIRST try, GOOD JOB!!!")

        if count != 1:
            print("You have DONE it in this amount of tries", count ,"GOOD JOB")

        

menu()

##  MAIN MENU
##  --------------------
##      1. Adding Random Numbers
##      2. Subtracting Random Numbers
##      3. Exit
##  Please enter one of the menu options: 1
##     If 1 is entered
##  7
##  + 79
##  Enter number: 86
##     If you answered rght
##  you won
##  You have DONE it in this amount of tries 1 GOOD JOB
##  MAIN MENU
##  --------------------
##      1. Adding Random Numbers
##      2. Subtracting Random Numbers
##      3. Exit
##  Please enter one of the menu options: 


    


 
