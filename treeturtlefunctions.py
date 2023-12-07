import turtle
michaelangelo = turtle.Turtle()

def draw_square(side_length: float) -> None:
    for i in range(4):
        michaelangelo.forward(side_length)
        michaelangelo.left(90)
def draw_tree(level: int, height:int) -> None:
    """a recursove funtion that draws a tree with intitial geven height
    
    
    Params:
    level - number repersenting levels of branches
    height - height of main trunk in pixels
    """
    if level > 0:
        # 1 draw the branch
        michaelangelo.forward(height)
        # 2 turn to the left 
        michaelangelo.left(39)
        # 3 draw a smaller tree
        draw_tree(level-1, height/1.5)
        # 4 turn to the right
        michaelangelo.right(39*2)
        # 5 draw a smaller tree
        draw_tree(level-1, height/1.5)
        # 6 move back to the begining
        michaelangelo.left(39)
        michaelangelo.back(height)
    else:
        michaelangelo.color("brown")
        michaelangelo.color("green")
        michaelangelo.stamp()
        michaelangelo.color("brown")
        
def draw_trees(level: int, height:int) -> None:
    """a recursove funtion that draws a tree with intitial geven height
    
    
    Params:
    level - number repersenting levels of branches
    height - height of main trunk in pixels
    """
    if level > 0:
        # 1 draw the branch
        michaelangelo.forward(height)
        # 2 turn to the left 
        michaelangelo.left(39)
        # 3 draw a smaller tree
        draw_trees(level-1, height * .75)
        
        # 4 turn to the right
        michaelangelo.right(39*2)
        # 5 draw a smaller tree
        draw_trees(level-1, height * .75)
        draw_tree(4, 35)
        # 6 move back to the begining
        michaelangelo.left(39)
        michaelangelo.back(height)
    else:
        michaelangelo.color("brown")
        michaelangelo.color("green")
        michaelangelo.stamp()
        michaelangelo.color("brown")
michaelangelo.hideturtle()
michaelangelo.left(90)
michaelangelo.color("brown")
michaelangelo.width(4)
michaelangelo.speed(900)

draw_trees(4, 175)
turtle.done()