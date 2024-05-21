import turtle
import random

def boardFull(gamestate):
    #if theres a 2 anywhere that means that space is empty
    for i in range(3):
        for j in range(3):
            if(gamestate[i][j] == 2):
                return False
            
    return True

def validspace(gamestate, row, col):
    return gamestate[row][col] == 2

def ifwon(player, gamestate, draw = False):
    #check rows
    for i in range(3):
        if(gamestate[i][0] == gamestate[i][1] and gamestate[i][1] == gamestate[i][2] and gamestate[i][0] == player):
            if(draw):
                drawHorzLine(player, i)
            return True
        
    #check cols
    for j in range(3):
        if(gamestate[0][j] == gamestate[1][j] and gamestate[1][j] == gamestate[2][j] and gamestate[0][j] == player):
            if(draw):
                drawVertLine(player, i)
            return True
        
    #check diags
    if(gamestate[0][0] == gamestate[1][1] and gamestate[1][1] == gamestate[2][2] and gamestate[0][0] == player):
        if(draw):
            drawDiagLine(player, 0)
        return True
    
    if(gamestate[0][2] == gamestate[1][1] and gamestate[1][1] == gamestate[2][0] and gamestate[1][1] == player):
        if(draw):
            drawDiagLine(player, 2)
        return True


#figures out if computer can win and returns the cell that it needs to play, returns -1 if it cant
def canWin(gamestate, player):
    for i in range(9):
        if(gamestate[i // 3][i % 3] == 2):
            gamestate[i // 3][i % 3] = player

            if(ifwon(player, gamestate)):
                gamestate[i // 3][i % 3] = 2
                return i
            
            gamestate[i // 3][i % 3] = 2
    
    return -1
    

    


def drawX(row, col, height, width, turt):
    x = width * col / 3- width / 3 
    y = -1 * (height * row / 3 - height / 3)

    turt.penup()
    turt.pencolor("blue")
    turt.goto(x,y)
    turt.right(45)
    turt.pendown()
    turt.forward(height / 6)
    turt.right(180)
    turt.forward(height / 3)
    turt.penup()
    turt.goto(x,y)
    turt.right(90)
    turt.pendown()
    turt.forward(height / 6)
    turt.right(180)
    turt.forward(height / 3)
    turt.setheading(90)

def drawO(row, col, height, width, t):
    x = width * col / 3 - width / 3 + height / 7
    y = (-1 * (height * row / 3 - height / 3))

    t.penup()
    t.goto(x,y)
    t.pencolor("red")
    t.pendown()
    t.circle(height / 7)

def drawHorzLine(player, row):
    y = row * h - h

    t.width(4)
    if(player == 1):
        t.pencolor("blue")
    else:
        t.pencolor("red")
    
    t.speed(2)
    t.penup()
    t.goto(-1*w/2, y)
    t.setheading(0)
    t.pendown()
    t.forward(w)
    t.width(1)

def drawVertLine(player, col):
    x = 1

def drawDiagLine(player, diag):
    x = 1


def drawBoard():
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
    


h = 540
w = 540

s = turtle.Screen()
s.setup(w, h)
t = turtle.Turtle()
turtle.title("Tic-Tac-Toe")
done = 0


while(done == 0):
    t.clear()
    drawBoard()
    gamestate = [[2,2,2],[2,2,2],[2,2,2]]
    winner = False

    while(not boardFull(gamestate) and not winner):
        print("==========PLAYER 1 TURN==========")
        x = int(input("Which cell will you select: ")) - 1

        while((x < 0 or x > 8) or not validspace(gamestate, x // 3, x % 3)):
            x = int(input("ERROR: Cell is not valid, choose another: ")) - 1
        
        gamestate[x // 3][x % 3] = 1
        drawX(x // 3, x % 3, h, w, t)

        winner = ifwon(1, gamestate)

        if(not winner):
            if(not boardFull(gamestate)):
                print("==========COMPUTER TURN==========")
                win = canWin(gamestate, 0)

                if(win > -1):
                    gamestate[win // 3][win % 3] = 0
                    print("Computer: I choose cell " + str(win + 1))
                    drawO(win // 3, win % 3, h, w, t)
                else:
                    loss = canWin(gamestate, 1)

                    if(loss > -1):
                        gamestate[loss // 3][loss % 3] = 0
                        print("Computer: I choose cell " + str(loss + 1))
                        drawO(loss // 3, loss % 3, h, w, t)
                    elif(gamestate[1][1] == 2):
                        gamestate[1][1] = 0
                        print("Computer: I choose cell 5")
                        drawO(1,1,h,w,t)
                    else: 
                        p = -1

                        while(p < 0 or p > 8 or not validspace(gamestate, p // 3, p % 3)):
                            p = random.randint(0,8)
                    
                        gamestate[p // 3][p % 3] = 0
                        print("Computer: I choose cell " + str(p + 1))
                        drawO(p // 3, p % 3, h, w, t)
        else:
            print("Player 1 Wins!")
            ifwon(1, gamestate, True)

        if(ifwon(0, gamestate)):
            winner = True
            print("Computer Wins!")
            ifwon(0, gamestate, True)
        
        if(boardFull(gamestate)):
            print("Tie")

    done = int(input("Finished?: "))
