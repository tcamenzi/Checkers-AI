from Globals import *

'''
This has all the rules for  checkers. It
1) lists all possible moves given a board
2) updates the game state based on your moves
'''
class Environment:

	@staticmethod
	def getStartRowState(row):
	    first = ('R','','R','','','','B','')
	    second = ('','R','','','','B','','B')
	    return (first[row], second[row])*4

	@staticmethod
	def getStartState():
		return tuple(Environment.getStartRowState(row) for row in range(NUM_SQUARES))

	@staticmethod
	def updateState(state, move):
		mutableState = list(list(row) for row in state)
		for startstate, endstate in zip(move[:-1], move[1:]):
			startrow = startstate[0]
			startcol = startstate[1]

			endrow = endstate[0]
			endcol = endstate[1]

			piece = mutableState[startrow][startcol]
			mutableState[startrow][startcol] = ''

			# if not environment.isAdjacnet(startstate, endstate): #you jumped a piece
			#If you jumped a piece, set the in-between to be empty.
			#If you didn't jump a piece, this sets the beginning/ending square to be emtpy anyways.
			midrow = (startrow+endrow)/2
			midcol = (startcol+endcol)/2
			mutableState[midrow][midcol] = ''

			mutableState[endrow][endcol] = piece

		updatedState = tuple(tuple(row) for row in mutableState)
		return updatedState 

	@staticmethod
	def inBounds(row,col):
		return row>=0 and row<NUM_SQUARES and col>=0 and col<NUM_SQUARES

	@staticmethod
	def getDiagonals(row, col):
		for rowoffset in (-1,1):
			for coloffset in (-1,1):
				if Environment.inBounds(row+rowoffset, col+coloffset):
					yield (row+rowoffset, col+coloffset)

	@staticmethod
	def canJump(state, row, col, diagrow, diagcol):
		endrow = row+2*(diagrow-row)
		endcol = col+2*(diagcol-col)
		return Environment.inBounds(endrow, endcol) and state[endrow][endcol]=='' #can jump

	@staticmethod
	def handleJump(state, row, col, diagrow, diagcol, color):
		endrow = row+2*(diagrow-row)
		endcol = col+2*(diagcol-col)
		move = ((row, col), (endrow, endcol))
		statePostJump = Environment.updateState(state,move)
		yield move
		for postJumpMove in Environment.getJumpsForPiece(statePostJump, endrow, endcol, color):
			yield move+postJumpMove

	@staticmethod
	def getJumpsForPiece(state,row,col,color):
		for diagrow, diagcol in Environment.getDiagonals(row,col):
			if opposing(color) in state[diagrow][diagcol]: #opponent piece there
				print "opposing piece at: ", diagrow, diagcol
				print "color: ", color, "opposing: ", opposing(color) 
				if Environment.canJump(state, row, col, diagrow, diagcol): #is the landing spot clear?
					for move in Environment.handleJump(state, row, col, diagrow, diagcol, color):
						yield move 
	@staticmethod
	def getMovesForPiece(state,row,col, color):
		print "row, col: ", row, col 
		for diagrow, diagcol in Environment.getDiagonals(row,col):
			# print "diagrowcol:" , diagrow, diagcol 
			if state[diagrow][diagcol]=='': #empty
				yield ((diagrow, diagcol),)

		for move in Environment.getJumpsForPiece(state,row,col,color):
			yield move 


	@staticmethod
	def getMoves(state, color):
		print "color: ", color
		for row in range(len(state)):
			for col in range(len(state[0])):
				if color in state[row][col]:
					for move in Environment.getMovesForPiece(state, row, col, color):
						yield ((row,col),) + move 




