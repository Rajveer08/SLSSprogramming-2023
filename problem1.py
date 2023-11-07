#rajveer
name=input("what is your name ")
contNum=-1
print(f"hello {name} its nice to meet you")
totalNum=0
continents=["asia","europe","north america","south america","australia", "africa","antartica"]

for continent in continents:
    contNum+=1
    contQ=input(f"have you been to {continents[contNum]} ")
    if contQ.lower()=="yes":
        totalNum+=1
print(f"you have visited {totalNum}/7 continents")