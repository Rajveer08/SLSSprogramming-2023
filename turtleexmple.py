import turtle
TURTLE_MAGNITUDE = 20
michaelangelo = turtle.Turtle()

print("""to give commands, type:
    F - to go forward
    L - to go left 
    R - to go right
    B - to go backwards
    X - to stop
    + - to raise speed
    -  to lower speed""")

while True:
    
    command = input(" ")
    if command.strip(",.?! ").lower()== "+":
        TURTLE_MAGNITUDE+=20
    elif command.strip(",.?! ").lower()== "-":
        TURTLE_MAGNITUDE-=20
    elif command.strip(",.?! ").lower()== "f":
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command.strip(",.?! ").lower()== "b":
        michaelangelo.forward(-TURTLE_MAGNITUDE)
    elif command.strip(",.?! ").lower()== "l":
        michaelangelo.left(90)
    elif command.strip(",.?! ").lower()== "r":
        michaelangelo.right(90)
    elif command.strip(",.?! ").lower()== "x":
        break
