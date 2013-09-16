import random

class RandomAgent:
	def __init__(self, environment, color):
		self.environment = environment 
		self.color = color 

	def nextMove(self, state):
		moves = [item for item in self.environment.getMoves(state, self.color)]
		if len(moves)==0:
			return None
		rint = random.randint(0,len(moves)-1)
		move = moves[rint]
		return move 

	def noteWin(self):
		pass

	def noteLoss(self):
		pass