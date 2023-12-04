#calculate how many calories the elf carrying the most has
elves=[]
with open("./aoc2022day1.txt") as f:
    current_cals=0
    for line in f:
        if line.strip():
            current_cals += int(line.strip())
        else:
            elves.append(current_cals)
            current_cals=0
biggest_cals=0
for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf
sorted_elves = sorted(elves)
top_three=sorted_elves[-3:]
top
print(max(elves))
print(sum(sorted(elves)[-3: ]))