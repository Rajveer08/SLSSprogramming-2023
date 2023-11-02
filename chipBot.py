
totalRating=0


questions=["how do you rate the crispiness from a scale of 1 to 5"," hows the crisp from 1 to 5", "how to crunch from 1 to 5"]

for question in questions:
    print(question)
    user_rating=int(input(" "))
    totalRating+=user_rating

 

averageRating= totalRating / len(questions)
print(f"the average rating of the chip is: {averageRating}")