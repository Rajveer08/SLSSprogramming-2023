#Rajveer
#november 16 2023s
question = ["Did you eat: ","Did you study: ","Did you do your laundry: ","Did you call your grandma: "]
total_score=0
#asks questions
for questions in question:
    parental_question=input(questions)
    if parental_question.lower()=="yes":
        total_score+=1

#calculates if bot should come
if total_score==0:
    print("im coming over")
elif total_score <3:
    print("ok")

elif total_score <5:
    print("good")

