from Globals import *


import pygame
import sys
pygame.init()

DISPLAY_SIZE = 400
SQUARE_SIZE = DISPLAY_SIZE / NUM_SQUARES
PIECE_RADIUS = int(   (SQUARE_SIZE/2)*.87   )
RED_PIECE_COLOR = (255,0,0)
RED_SQUARE_COLOR = (200,0,0)

KING_FONT = pygame.font.Font(None, 40)
FONT_COLOR = (100,100,100)
CIRCLE_OUTLINE_WIDTH = 0
CIRCLE_OUTLINE_COLOR = BLUE

window = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))

'''
This class handles all graphics involved for checkers. It
- draws the board
- lets you highlight squares when the user selects pieces
'''
class GUI:

    boardState = None
    @staticmethod 
    def draw(state):
        GUI.boardState = state
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                color = RED_SQUARE_COLOR if ((row+col)%2) else GREY #alternate based on even/odd sum
                GUI.drawSquare(row, col, color)
                GUI.drawStateSquare(row,col, state[row][col])
        pygame.display.flip()

    @staticmethod
    def drawSquare(row,col,color):
        rowcoord = row*SQUARE_SIZE
        colcoord = col*SQUARE_SIZE
        rectwidth = rectheight = SQUARE_SIZE
        pygame.draw.rect(window, color, (colcoord, rowcoord, rectwidth, rectheight))
           
    @staticmethod
    def highlightSquare(row,col,color=YELLOW):
        GUI.drawSquare(row,col,color)
        GUI.drawStateSquare(row, col, GUI.boardState[row][col])
        pygame.display.flip()

    
    @staticmethod
    def drawStateSquare(row,col,stateSquare):
        #stateSquare has a B for black, R for red
        # and K for king
        rowcenter = int( (row+.5)*SQUARE_SIZE)
        colcenter = int((col+.5)*SQUARE_SIZE)
        color = RED_PIECE_COLOR if 'R' in stateSquare else BLACK if 'B' in stateSquare else None
        if color:
            GUI.drawCircle(rowcenter, colcenter, color)

             #Now draw king if needed
            if 'K' in stateSquare:
                kcolor = GREY
                text = KING_FONT.render('K', True, FONT_COLOR)
                tw = text.get_width()
                th = text.get_height()
                window.blit(text, [colcenter-tw/2, rowcenter - th/2])

    @staticmethod
    def drawCircle(rowcenter, colcenter, color):
        pygame.draw.circle(window, CIRCLE_OUTLINE_COLOR, (colcenter, rowcenter), PIECE_RADIUS, CIRCLE_OUTLINE_WIDTH)
        pygame.draw.circle(window, color, (colcenter, rowcenter), PIECE_RADIUS - CIRCLE_OUTLINE_WIDTH)

    @staticmethod
    def deselectAll():
        GUI.draw(GUI.boardState)

    @staticmethod
    def selectSquare():
        clock = pygame.time.Clock()
        
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    done=True
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    row = pos[1]/SQUARE_SIZE
                    col = pos[0]/SQUARE_SIZE
                    
                    return row,col
                    
                    
            clock.tick(20)
        pygame.quit()
        sys.exit(0)
           
                
                
                


 

