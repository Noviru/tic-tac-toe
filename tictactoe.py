import pygame as pg
import time



#Vita linjer

#Brädet
#Globala variabler
board = [[None]*3, [None]*3,[None]*3]
width = 600
height = 600
color = (255, 255, 255)
pg.init()
pg.display.set_caption("Tic tac toe")
screen = pg.display.set_mode([width, height])
screen.fill(color)
pg.display.flip()
xImg = pg.image.load('X.png').convert_alpha()
oImg = pg.image.load('O.png').convert_alpha()
winner = None
turn = "X"





def main():
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
    if pos != None:
        if turn == "X":  
            screen.blit(xImg,pos)
            turn = "O"
        elif turn == "O":
            screen.blit(oImg,pos)
            turn = "X"
        pg.display.flip()
        #Har någon vunnit?
        checkWin()
        if winner != None:
            stopGame()
    
    
    

def stopGame():
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render(f'The winner is {winner}', True,green,blue)
    screen.blit(text,(200,200))


def checkWin():
    #Tittar om någon vinner vågrät
    verticalList = []
    diagonalList1 = []
    diagonalList2 = []
    counter1 = 0
    counter2 = 2
    for row in board:
        verticalList.append(row[0])
        diagonalList1.append(row[counter1])
        diagonalList2.append(row[counter2])
        counter2 -= 1
        counter1 += 1
        if row.count("X") == len(row):
            winner = "X"
        elif row.count("O") == len(row):
            winner = "O"
    
         


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

#Zanton 
#Kordinater för hörnen på kvadtaterna i brädet:
#board[0][0] == (0,0), (200,0),(200,200),(0,200) (0,0) - (0,200) (200, 0) - (200,200)
#board[0][1] == (200,0), (400,0),(200,200),(0,200)
#Tar in positionen där musen trycktes.
#Här ska rätt board ruta uppdateras 
#
def updateBoard(pos):
    #Board variabeln
    #Vems tur
    #(Resetgame)
    #Skickas postionen som bilden ska sättas ut på.
    posForImage = getImgCoordinate(pos)
    drawUpdates(posForImage)
    print(board)



main()