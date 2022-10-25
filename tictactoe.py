import pygame as pg
from random import randint
import time

#Vita linjer

#Brädet
#Globala variabler
board = [[None]*3, [None]*3,[None]*3]
width = 600
height = 600
color = (255, 255, 255)
pg.init()
screen = pg.display.set_mode([width, height])
screen.fill(color)
pg.display.flip()
xImg = pg.image.load('X.png').convert_alpha()
oImg = pg.image.load('O.png').convert_alpha()
winner = None
turn = "X"
botPlaying = False





def mainMenu():
    drawMenu()
    while True:
        for ev in pg.event.get():      
            if ev.type == pg.QUIT:
                pg.quit()
            #(200,75), (400,75),(200,135,) (400,135) #Twoplayer
            #(200,175), (400,175),(200,235), (400,235)#One player
            if ev.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if 200 <= pos[0] <= 400 and 75 <= pos[1] <= 135:
                    mainGame()
                    
                elif 200 <= pos[0] <= 400 and 175 <= pos[1] <= 235:
                    global botPlaying
                    print("Bot playing")
                    botPlaying = True
                    mainGame()
                    
                
def drawMenu():
    pg.display.set_caption("Main menu")
    screen = pg.display.set_mode([width, height])
    screen.fill(color)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    font = pg.font.Font('freesansbold.ttf', 32)

    #Text för twoPlayer
    #Koordinater för texten - 
    textTwoPlayer = font.render('Two player' , True , color_dark)
    textRectTwo = textTwoPlayer.get_rect()
    textRectTwo.center = (300,100)
    screen.blit(textTwoPlayer, textRectTwo)
    pg.draw.rect(screen, color_dark, pg.Rect(200, 75, 200, 60),  2)
    #Text för onePlayer
    textOnePlayer = font.render('One Player' , True , color_dark)
    textRectOne = textOnePlayer.get_rect()
    textRectOne.center = (300,200)
    screen.blit(textOnePlayer, textRectOne)
    pg.draw.rect(screen, color_dark, pg.Rect(200, 175, 200, 60),  2)
    #Text för tictactoe
    text = font.render('Tic Tac Toe' , True , color_dark)
    textRect = textOnePlayer.get_rect()
    textRect.center = (300,50)    
    screen.blit(text, textRect)
    pg.display.flip()

def mainGame():
    #Variabler för rutan
    drawGrid()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == 1025 and winner == None:
                pos = pg.mouse.get_pos()
                print(pos)
                updateBoard(pos)
            
    
#Ritar spelplanen
def drawGrid():
    #Ta bort menyn genom att färga allt vitt.
    screen.fill(color)
    black = ((0,0,0))
    pg.draw.line(screen, black, (200, 0), (200, 600))
    pg.draw.line(screen, black, (400, 0), (400, 600))
    pg.draw.line(screen, black, (600, 0), (600, 600))
    pg.draw.line(screen, black, (0, 200), (600, 200))
    pg.draw.line(screen, black, (0, 400), (600, 400))
    pg.display.flip()


#Anton
#win boolean,
def drawUpdates(pos):
    global turn
    checkWin()
    print(f'the winner is {winner}')
    stopGame(checkDraw())
    if pos != None:
        if turn == "X":  
            screen.blit(xImg,pos)
            turn = "O"
        elif turn == "O":
            screen.blit(oImg,pos)
            turn = "X"
        pg.display.flip()
        #Har någon vunnit?

        
    
    
    

def stopGame(draw):
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pg.font.Font('freesansbold.ttf', 32)
    print("Nu är jag i stopGame()")
    if winner != None:
        text = font.render(f'The winner is {winner}', True,green,blue)
        screen.blit(text,(200,200))
    if draw == True:
        text = font.render(f'Draw', True,green,blue)
        screen.blit(text,(200,200))
    pg.display.flip()

def horizontalWin():
    global winner
    for row in board:
        if row.count("X") == len(row):
            winner = "X"
        elif row.count("O") == len(row):
            winner = "O"

def verticalWin():
    global winner
    line1 = []
    line2 = []
    line3 = []
    for row in board:
        line1.append(row[0])
        line2.append(row[1])
        line3.append(row[2])
    if line1.count("X") == len(line1) or line2.count("X") == len(line1) or line3.count("X") == len(line1):
        winner = "X"
        print("X Vann")
    if line1.count("O") == len(line1) or line2.count("O") == len(line1) or line3.count("O") == len(line1):
        winner = "O"


# 0, 0 = 25,25
# 0, 1, 25, 225
# 0, 2, 25, 425
# 1,0, 225, 25
# 1,1, 225, 225
# 1, 2, 225, 425
def getPosFromIndex(index):
    yIndex = 0
    xIndex = 0
    for row in board:
        for square in row:
            if index[0] == yIndex and index[1] == xIndex:
                return (index[1]*200+25,index[0]*200+25)
            xIndex += 1
        yIndex += 1
        xIndex = 0
def diagonalWin():


    global winner
    diagonalList1 = []
    diagonalList2 = []
    counter1 = 0
    counter2 = 2
    for row in board:
        diagonalList1.append(row[counter1])
        diagonalList2.append(row[counter2])  
        counter2 -= 1
        counter1 += 1
    if diagonalList1.count("O") == len(diagonalList1) or diagonalList2.count("O") == len(diagonalList2):
        winner = "O"
    if diagonalList1.count("X") == len(diagonalList1) or diagonalList2.count("X") == len(diagonalList2):
        winner = "X"
def checkWin():
    horizontalWin()
    diagonalWin()
    verticalWin()

def checkDraw():
    emptySquares = getEmptySquares()
    print("Tomma rutor")
    print(emptySquares)
    if len(emptySquares) == 0:
        return True
    
def getEmptySquares():
    emptySquares = []
    boardIndex = 0
    rowIndex = 0
    for row in board:
        for square in row:
            tmpList = []
            if square == None:
                tmpList = [boardIndex,rowIndex]
                emptySquares.append(tmpList)
            rowIndex += 1
        boardIndex += 1
        rowIndex = 0
    return emptySquares

def botTurn():
    global turn
    emptySquares = getEmptySquares()
    countEmptySquares = len(emptySquares)-1
    randomNum = randint(0,countEmptySquares)
    index = emptySquares[randomNum]

    board[index[0]][index[1]] = turn
    print("Index:")
    print(index)
    pos = getPosFromIndex(index)
    print("Postition:")
    print(pos)
    drawUpdates(pos)




def getImgCoordinate(pos):
    global turn
    # 0 < pos[0] < 200, 0 < pos[1] < 200 ruta 1
    # 200 < pos[0] < 400, 0 < pos[1] < 200 ruta 2
    # 400 < pos[0] < 600, 0 < pos[1] < 200 ruta 3
    # 0 < pos[0] < 200, 200 < pos[1] < 400
    # 200 < pos[0] < 400, 200 < pos[1] < 400
    # 400 < pos[0] < 600, 200 < pos[1] < 400
    xCounter = 0
    yCounter = 0
    xIndex = 0
    yIndex = 0
    for row in board:
        for square in row:
            if xCounter < pos[0] < (xCounter+200) and yCounter < pos[1] < (yCounter+200):
                if board[yIndex][xIndex] == None:
                    board[yIndex][xIndex] = turn
                    return (xCounter+25),(yCounter+25) 
            xIndex += 1
            xCounter += 200   
        yIndex += 1 
        yCounter += 200
        xCounter = 0
        xIndex = 0


#Kordinater för hörnen på kvadtaterna i brädet:
#board[0][0] == (0,0), (200,0), (200,200),(0,200) (0,0) - (0,200) (200, 0) - (200,200)
#board[0][1] == (200,0), (400,0),(200,200),(0,200)
#Tar in positionen där musen trycktes.
def updateBoard(pos):
    global botPlaying
    #Board variabeln
    #Vems tur
    #(Resetgame)
    #Skickas postionen som bilden ska sättas ut på.
    posForImage = getImgCoordinate(pos)
    drawUpdates(posForImage)
    print("Board before bot")
    print(board)
    if botPlaying == True and posForImage != None and winner == None:
        time.sleep(1)
        print("Skickas till funktionen")
        botTurn()
    print(board)



mainMenu()