NUM_SQUARES = 8
COLORS = ('R', 'B')

def opposing(color):
	if color == COLORS[0]:
		return COLORS[1]
	else:
		return COLORS[0]
