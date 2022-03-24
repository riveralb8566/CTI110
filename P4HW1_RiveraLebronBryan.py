# grade calculator
def main():
    grade = 0
    total = 0
    score_list = []

    num = int(input("Enter number of scores to total: "))

    for i in range(0, num):
        score = int(input("Enter score #" + str(i + 1)+ ": "))
        while score < 0 or score > 100:
            print("\nINVALID Score!!!!")
            print("Score should be between 0 and 100")
            score = int(input("Enter score #" + str(i + 1)+ " again: "))
        score_list.append(score)
    lowest = min(score_list)
    score_list.remove(lowest)
    print("\n--------------Results-----------")
    print("Lowest Score  : ", lowest)
    print("Modified List : ", score_list)
    average = sum(score_list)/ (num - 1)
    print("Scores Average: ", average)
    if average > 90:
        grade = "A"
    elif average > 80:
        grade = "B"
    elif average > 70:
        grade = "C"
    elif average < 69:
        grade = "F"
    print("Grade         : ", grade)
    print("----------------------------------")
        
# If enter numbers score of scores to total: 4
# Enter score #1: 70
# Enter score #2: 60
# Enter score #3: 100
# Enter score #4: 90
#
#  
# Print respones 
# --------------Results-----------
# Lowest Score  :  60
# Modified List :  [70, 100, 90]
# Scores Average:  86.66666666666667
# Grade         :  B
# ----------------------------------

main()
