
yes= True

profile=[
    "Bubble World",
    "Chef Hung",
    "Uncle Fatihs's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]    
most_similar_score = 0
most_similar_name = ""
least_similar_score = 10
least_similar_name = ""
with open("./data.csv") as f:
    header = f.readline()

    for line in f:
        current_likes = line.split(",")

        current_name = current_likes[1]

        current_sim_score = 0

        for item in profile:
            if item in current_likes:
                current_sim_score+=1
        
        print(f"{current_name} - score: {current_sim_score}")

        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name
        if current_sim_score < least_similar_score:
            least_similar_score = current_sim_score
            least_similar_name = current_name
print("Most similar person")
print(f"{most_similar_name}- Score: {most_similar_score}")
print("Least similar person")
print(f"{least_similar_name}- Score: {least_similar_score}")

