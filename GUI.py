import pygame
pygame.init()

DISPLAY_SIZE = 400
NUM_SQUARES = 8
SQUARE_SIZE = DISPLAY_SIZE / NUM_SQUARES
PIECE_RADIUS = int(   (SQUARE_SIZE/2)*.87   )
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GREY = (40,40,30)
WHITE = (255,255,255)
KING_FONT = pygame.font.Font(None, 40)
FONT_COLOR = (100,100,100)
CIRCLE_OUTLINE_WIDTH = 0

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
                color = RED if ((row+col)%2) else GREY #alternate based on even/odd sum
                GUI.drawSquare(row, col, color)
        pygame.display.flip()

    @staticmethod
    def drawSquare(row,col,color):
        rowcoord = row*SQUARE_SIZE
        colcoord = col*SQUARE_SIZE
        rectwidth = rectheight = SQUARE_SIZE
        pygame.draw.rect(window, color, (rowcoord, colcoord, rectwidth, rectheight))
           
    @staticmethod
    def highlightSquare(row,col,color):
        GUI.drawSquare(row,col,color)
        GUI.drawStateSquare(row, col, GUI.boardState[row][col])
        pygame.display.flip()

    
    @staticmethod
    def drawStateSquare(row,col,stateSquare):
        #stateSquare has a B for black, R for red
        # and K for king
        rowcenter = int( (row+.5)*SQUARE_SIZE)
        colcenter = int((col+.5)*SQUARE_SIZE)
        color = RED if 'R' in stateSquare else BLACK if 'B' in stateSquare else None
        if color:
            GUI.drawCircle(rowcenter, colcenter, color)

             #Now draw king if needed
            if 'K' in stateSquare:
##                kcolor = BLACK if color==RED else RED #opposite color so you can see it
                kcolor = GREY
                text = KING_FONT.render('K', True, FONT_COLOR)
                tw = text.get_width()
                th = text.get_height()
                window.blit(text, [rowcenter-tw/2, colcenter - th/2])

    @staticmethod
    def drawCircle(rowcenter, colcenter, color):
        outlineColor = BLACK if color==RED else RED
        pygame.draw.circle(window, outlineColor, (colcenter, rowcenter), PIECE_RADIUS, CIRCLE_OUTLINE_WIDTH)
        pygame.draw.circle(window, color, (colcenter, rowcenter), PIECE_RADIUS - CIRCLE_OUTLINE_WIDTH)

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
           
                
                
                

        
            
            
state = []        
for i in range(8):
    state.append(['RK']*8)
GUI.draw(state)
GUI.drawStateSquare(0,0,'KB')
GUI.highlightSquare(0,0,YELLOW)
pygame.display.flip()
print GUI.selectSquare()

