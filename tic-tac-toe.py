import turtle

def gamedone(gamestate):
    for i in range(3):
        for j in range(3):
            if(gamestate[i][j] == 2):
                return False
            
    return True

def validspace(gamestate, row, col):
    return gamestate[row][col] == 2

def ifwon(player, gamestate):
    #check rows
    for i in range(3):
        if(gamestate[i][0] == gamestate[i][1] and gamestate[i][1] == gamestate[i][2] and gamestate[i][0] == player):
            return True
        
    #check cols
    for j in range(3):
        if(gamestate[0][j] == gamestate[1][j] and gamestate[1][j] == gamestate[2][j] and gamestate[0][j] == player):
            return True
        
    #check diags
    if(gamestate[0][0] == gamestate[1][1] and gamestate[1][1] == gamestate[2][2] and gamestate[0][0] == player):
        return True
    
    return gamestate[0][2] == gamestate[1][1] and gamestate[1][1] == gamestate[2][0] and gamestate[1][1] == player
    


def drawX(row, col, height, width, turt):
    x = width * col / 3- width / 3
    y = -1 * (height * row / 3 - height / 3)

    turt.penup()
    turt.goto(x,y)
    turt.right(45)
    turt.pendown()
    turt.forward(150)
    turt.right(180)
    turt.forward(300)
    turt.penup()
    turt.goto(x,y)
    turt.right(90)
    turt.pendown()
    turt.forward(150)
    turt.right(180)
    turt.forward(300)
    turt.setheading(90)
    


h = 900
w = 900

s = turtle.Screen()
s.setup(w, h)
t = turtle.Turtle()
turtle.title("Tic-Tac-Toe")

# setup
t.speed(100)
t.ht()
t.penup()
t.goto(-1*w/2 + w/3,h/2)
t.pendown()
t.right(90)
t.forward(h)
t.penup()
t.goto(-1*w/2 + 2*w/3, -1*h/2)
t.left(180)
t.pendown()
t.forward(h)
t.penup()
t.goto(w/2, -1*h/2 + h/3)
t.left(90)
t.pendown()
t.forward(w)
t.penup()
t.goto(-1*w/2, -1*h/2 + 2*h/3)
t.left(180)
t.pendown()
t.forward(w)

gamestate = [[2,2,2],[2,2,2],[2,2,2]]
winner = False

while(not gamedone(gamestate) and not winner):
    print("==========PLAYER 1 TURN==========")
    x = int(input("Which cell will you select: ")) - 1

    while((x < 0 or x > 8) or not validspace(gamestate, x // 3, x % 3)):
        x = int(input("ERROR: Cell is not valid, choose another: ")) - 1
    
    gamestate[x // 3][x % 3] = 1
    drawX(x // 3, x % 3, h, w, t)

    winner = ifwon(1, gamestate)

    if(not winner):
        print("==========COMPUTER TURN==========")
    else:
        print("Player 1 Wins!")


