# CTI-110
# P2HW2 - Score Avg
# Bryan Lee Rivera Lebron 
# 2/24/2022
#


score_list = []
score = float(input("Enter score #1: "))
score_list.append(score)
score = float(input("Enter score #2: "))
score_list.append(score)
score = float(input("Enter score #3: "))
score_list.append(score)
score = float(input("Enter score #4: "))
score_list.append(score)
score = float(input("Enter score #5: "))
score_list.append(score)
score = float(input("Enter score #6: "))
score_list.append(score)
score = float(input("Enter score #7: "))
score_list.append(score)


lowest = min(score_list)
score_list.remove(lowest)


total = sum(score_list)
length = len(score_list)
average = total/length


print('--------------Results-----------')
print('Lowest Score', lowest)
print('Modified List', score_list)
total = sum(score_list)
print("Scores Average: ",format(average,'.2f'))
print('----------------------------------')

# If Enter score #1: 12
# Enter score #2: 75.9
# Enter score #3: 23.7
# Enter score #4: 27
# Enter score #5: 79
# Enter score #6: 98.9
# Enter score #7: 89
#
#   Print response
#       --------------Results-----------
#       Lowest Score 12.0
#       Modified List [75.9, 23.7, 27.0, 79.0, 98.9, 89.0]
#       Scores Average:  65.58
#       ----------------------------------
