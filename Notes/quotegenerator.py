# quote generator
# author: rajveer
# date 09 19 2023
import random 
quotes=["Love what you do to do great work.",
"Remember the silence of friends, not the words of enemies.",
"Life happens when plans change.",
"Doubt limits tomorrow's possibilities.",
"Rising after a fall is true glory.",
"Life goes on.",
"Be yourself; it's the greatest accomplishment.",
"Courage counts more than success or failure.",
"Triumph of evil requires inaction from good.",
"Infinite universe, human stupidity.",
"Create your future.",
"Don't just exist; live.",
"You decide your destiny.",
"Change is life's constant.",
"Purpose is happiness.",
"Start where you are, change the ending.",
"Happiness leads to success.",
"Judge days by seeds planted, not harvest reaped.",
"True wisdom is knowing you know nothing.",
"Remember the silence of friends."]
yes=1
while yes == 1:
    quoteAsk= input("do you want a quote ")
    quote=random.choice(quotes)
    if quoteAsk=="yes":
        print(quote)
    else:
        print("i hate you")
         