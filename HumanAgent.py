from Globals import *

class HumanAgent:
	def __init__(self, GUI, environment, color):
		self.gui = GUI
		self.environment = environment 
		self.color = color 


	def getStartState(self, state):
		start = self.gui.selectSquare()
		while self.color not in state[start[0]][start[1]]: #highlight a correct square
			start = self.gui.selectSquare()
		self.gui.highlightSquare(start[0],start[1])
		return start 


	'''Return None if you click on quitstate.
	Else return the move you selected which is in 
	validMoves.'''
	def selectValidMove(self, validMoves, quitstate):
		print "validMoves: ", validMoves
		print 'quitstate: ', quitstate
		if len(validMoves)==0: #no valid moves, must quit
			return None

		for move in validMoves:
			self.gui.highlightSquare(move[0], move[1])

		curr = self.gui.selectSquare() 
		while curr not in validMoves and curr!=quitstate:
			curr = self.gui.selectSquare() 

		self.gui.deselectAll()

		if curr == quitstate:
			return None
		else:
			return curr 

	def attemptMove(self, state):
		start = self.getStartState(state)
		fullMove = (start,)

		possibleMoves = [move for move in self.environment.getMovesForPiece(state, start[0], start[1],self.color)] 
		print "possibleMoves: ", possibleMoves 

		validMoves = [move[1] for move in possibleMoves]
		print "validMoves here: ", validMoves 
		currState = self.selectValidMove(validMoves, start)
		if currState==None:
			self.gui.deselectAll()
			return None
		fullMove+=(currState,)

		index = 2
		while(True):
			validMoves = []
			for move in possibleMoves:
				if len(move)>index and move[index-1]==currState:
					validMoves.append(move[index])
			nextState = self.selectValidMove(validMoves, currState)
			if nextState == None: #done moving
				return fullMove
			#advance one
			fullMove+=(nextState,) 
			currState = nextState
			index+=1



		# for move in possibleMoves: #highlight adjacent ones 
		# 	adjacent = move[1]
		# 	self.gui.highlightSquare(adjacent[0], adjacent[1])

		# adjacentStates = set([move[1] for move in possibleMoves])
		# nextState = self.gui.selectSquare()
		# while nextState not in adjacentStates and nextState!=start: 
		# 	nextState = self.gui.selectSquare() 

		# self.gui.draw(state)

		# if nextState==start: #deselect it, choose a different piece
		# 	return None

		# #now, you've commited to making your move. If there are more
		# #jumps you can do, give the player options to do them.

		# currState = nextState 
		# index = 2
		# while(True):
		# 	adjacentStates = set([])
		# 	longmoves = [move for move in possibleMoves if len(move)>index]
		# 	for move in longmoves:
		# 		adjacent = move[index]
		# 		adjacentStates.add(adjacent)
		# 		self.gui.highlightSquare(adjacent[0], adjacent[1])

		# 	nextState = self.gui.selectSquare()
		# 	while nextState not in adjacentStates and nextState!=currState: 
		# 		nextState = self.gui.selectSquare() 
		# 	if nextState == currState:
		# 		return (start, currState)
		# 	index+=1


		


		

		# self.gui.draw(state)
		# #If they click on a piece and then decide not to move it,
		# #let them deselct by clicking on the same piece again.
		# if end==start:
		# 	return None

		# # self.gui.highlightSquare(end[0], end[1], GREEN)
		# # pathsToEnd = set([move for move in possibleMoves if move[-1]==end])
		# # print "paths to end"
		# # print len(pathsToEnd)
		# # print pathsToEnd
		# return (start, end)

	def nextMove(self, state):
		
		move = None
		while(move==None):
			move = self.attemptMove(state)
		print "MOVE BEING RETURNED: ", move 
		return move 

		