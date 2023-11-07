#Hashim Alkhatab made rajveer helped
#Date: November 6th 2023
#Problem: 2
#the score average = 0
score_average = 0
#asks how many courses the user is taking
courses = int(input("How many courses are you taking this semester?: "))
#for the amount of courses they have they will print that amount and ask you the rate it.
for courses in range(0,courses):
    rating_courses = int(input(f"What would you course out of 5: "))
    score_average += rating_courses
#this determines the average rating of the code and gives you a decent,average or bad feeback
courses = courses + 1
if score_average/courses <= 1:
    print(f"{score_average/courses} OUCH!")
elif score_average/courses <=3>1:
    print(f"{score_average/courses} Not a bad semester!")
else:
    print(f"{score_average/courses} Glad to hear it!")