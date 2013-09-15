class HumanAgent:
	def __init__(self, GUI, environment, color):
		self.gui = GUI
		self.environment = environment 
		self.color = color 

	def nextMove(self, state):
		start = self.gui.selectSquare()
		self.gui.highlightSquare(start[0],start[1])
		for move in self.environment.getMovesForPiece(state, start[0], start[1],self.color):
			print 'move: ', move
			endstate = move[-1]
			self.gui.highlightSquare(endstate[0],endstate[1])

		print start
		end = self.gui.selectSquare()
		print end 
		return (start, end)