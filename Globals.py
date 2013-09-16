NUM_SQUARES = 8
COLORS = ('R', 'B')

RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WHITE = (255,255,255)
GREY = (40,40,30)
BLACK = (0,0,0)

RED_DIRECTION = 1 #red goes down the board, ie row +=1
BLACK_DIRECTION = -1 #black goes up the board, ie row -=1

RED_KING_ROW = 7 #if a red piece gets to row 7, promote it to a king
BLACK_KING_ROW = 0

def opposing(color):
	if color == COLORS[0]:
		return COLORS[1]
	else:
		return COLORS[0]
