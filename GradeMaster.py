#GradeMaster

print("Welcome to the grade calculator.\n\
\nThis program will calculate your course grade point average.\n\
\nYou will need the name, weight, and score for each grading category in your course. Let's " "go!")

answer = input("\nWould you like to calculate a grade for another course? Enter yes or no: ")

while (answer.lower() !="no"):
    numCategories = int(input("How many grading categories does your course have? "))
    weights = 0
    weightedscore = 0
    
    for i in range(numCategories):
        name = input("Enter category name: ")
        weight = int(input("Enter the weight for this category: "))
        score = int(input("Enter the score earned: "))
        
        weights += weight
        weightedscore += weight/100 * score
    
    print("Total weight: ", weights)
    print("Your grade point average for this course is: ", weightedscore)
    answer = input("Would you like to calculate another course? Enter yes or no: ")
    
print("Goodbye") 
