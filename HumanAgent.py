from Globals import *

class HumanAgent:
	def __init__(self, GUI, environment, color):
		self.gui = GUI
		self.environment = environment 
		self.color = color 

	def noteWin(self):
		pass

	def noteLoss(self):
		pass

	# def learn(self, prevstate, nextstate, reward):
	# 	pass

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

		validMoves = [move[1] for move in possibleMoves]
		currState = self.selectValidMove(validMoves, start)
		if currState==None:
			self.gui.deselectAll()
			return -1
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

	def nextMove(self, state):
		
		moves = [item for item in self.environment.getMoves(state,self.color)] 
		if len(moves)==0:
			return None
		move = -1
		while(move==-1):
			move = self.attemptMove(state)
		return move 

		