age=int(input("how old are yout? "))

finalAge= age + 26

print(f"you will be {finalAge} in 2049")


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



burger=input("would you like a burger for 5$ (yes/no) ")
fries=input("would you like fries for 3$ (yes/no) ")
totalCost=0

if burger.lower()== "yes":
    totalCost+=5
if fries.lower()=="yes":
    totalCost+=3
tax=totalCost* 0.14    
print(f"${tax+ totalCost}")

