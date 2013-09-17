class MemorizeStateAgent:
	def __init__(self, environment, color):
		self.environment = environment 
		self.color = color 
		self.numMoves = 0
		self.lastState = None 
		self.stateValueFxn = {} #the afterstate fxn
		self.alpha = .2 #learning rate; shift 20% of way to observed value
		self.numWins = 0
		self.numLosses = 0

	#Use a greedy algo that memorizes game states.
	def nextMove(self, state):
		moves = [item for item in self.environment.getMoves(state, self.color)]
		bestMove = None
		bestValue = -1 #lowest possible 
		for move in moves:
			afterstate = self.environment.updateState(state, move)
			value = self.getValue(afterstate)
			if value >bestValue:
				bestValue = value
				bestMove = move 

		if bestMove == None: #no moves
			return bestMove  
		self.learn(bestValue) #get td error and update value
		self.lastState = self.environment.updateState(state, bestMove)
		return bestMove

	def learn(self, bestValue):
		if not self.lastState in self.stateValueFxn:
			self.stateValueFxn[self.lastState] = 1
		error = bestValue - self.getValue(self.lastState)
		update = error * self.alpha
		if update!=0:
			print ""
			print "update: ", update 
			for row in self.lastState:
				print row
			print ""
		self.stateValueFxn[self.lastState]+=update 

		

	def getValue(self, state):
		if state in self.stateValueFxn:
			return self.stateValueFxn[state]
		else:
			return 1 #be optimistic to explore

	def noteWin(self):
		print "win"
		self.learn(1) #last state has value of 1
		self.lastState = None
		self.numWins+=1
		if self.numWins%100==0:
			print "Agent Memorize has ", self.numWins, "wins"

	def noteLoss(self):
		print "loss"
		self.learn(-1)
		self.lastState = None 
		self.numLosses+=1
		if self.numLosses%100==0:
			print "Agent Memorize has ", self.numLosses, "losses"
	