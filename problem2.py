#i made this one hashim assisted
#rajveer mishra
#Date: November 6th 2023
#Problem: 1

score_average = 0
courses = int(input("How many courses are you taking this semester?: "))
for courses in range(0,courses):
    rating_courses = int(input(f"What would you course out of 5: "))
    score_average += rating_courses
    
print(score_average/rating_courses)
