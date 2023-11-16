#Rajveer
#november 16 2023

#variables
print("Please enter hobbies, seperated by a space")
person1=input("Person1: ").lower().split(" ")
person2=input("Person2: ").lower().split(" ")
common_hobby=0
#checks if hobbies are common
if person1[0] in person2:
    common_hobby+=1
if person1[1] in person2:
    common_hobby+=1
if person1[2] in person2:
    common_hobby+=1
#prints total common hobbies
print(f"You have {common_hobby} hobbies in common")