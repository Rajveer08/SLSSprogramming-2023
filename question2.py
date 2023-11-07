#This asks the JUDGES to input there score.
judge_one = float(input("Please enter the score you see reasonable judge number 'ONE'"))
judge_two = float(input("Please enter the score you see reasonable judge number 'TWO'"))
judge_three = float(input("Please enter the score you see reasonable judge number 'THREE'"))
judge_four = float(input("Please enter the score you see reasonable judge number 'FOUR'"))
judge_five = float(input("Please enter the score you see reasonable judge number 'FIVE'"))
#this adds up the total score of all the judges.
math = judge_one + judge_two + judge_three + judge_four + judge_five
#this checks if the total score is equal or greater then 50 and responds based on that.
if math >= 50:
    print(f"The judges have given a POSTIVE score of: {math}")
else:
    print(f"The judges have given a NEGATIVE score of: {math}")
