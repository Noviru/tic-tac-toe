import pygame as pg
import time
#Globala variabler

#Variabler för rutan
width = 600
height = 600
#Vita linjer
line_color = (0, 0, 0)
#Brädet
board = [[None]*3, [None]*3,[None]*3]

print(board)
#Skapar rutan



def main():
    drawBoard()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pq.quit()
                sys.exit()
        updateBoard()
    

def drawBoard():
    pg.init()
    pg.display.set_caption("Tic tac toe")
    screen = pg.display.set_mode([width, height])
    number_row = 3
    number_col = 3
    
def updateBoard():
    drawBoard()
main()