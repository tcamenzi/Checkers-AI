class MemorizeMonteCarlo:
	def __init__(self, environment, color):
		self.environment = environment 
		self.color = color 
		self.numMoves = 0
		self.visitedStates = [] 
		self.stateValueFxn = {} #the afterstate fxn
		self.alpha = .2 #learning rate; shift 20% of way to observed value
		self.numWins = 0
		self.numLosses = 0
		self.initial_value = 0 #1 to be exploratory, -1 no explore; 0 is neutral.

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
		self.visitedStates.append( self.environment.updateState(state, bestMove))
		return bestMove

	def learn(self, state, observedValue):
		if not state in self.stateValueFxn:
			self.stateValueFxn[state] = self.initial_value
		error = observedValue - self.getValue(state)
		update = error * self.alpha
		# if update!=0:
		# 	print ""
		# 	print "update: ", update 
		# 	for row in self.lastState:
		# 		print row
		# 	print ""
		self.stateValueFxn[state]+=update 

		

	def getValue(self, state):
		if state in self.stateValueFxn:
			return self.stateValueFxn[state]
		else:
			return self.initial_value

	def noteWin(self):
		print "win"
		for state in self.visitedStates:
			self.learn(state, 1)
		self.visitedStates = []
		self.numWins+=1
		if self.numWins%100==0:
			print "Agent Memorize has ", self.numWins, "wins"

	def noteLoss(self):
		print "loss"
		for state in self.visitedStates:
			self.learn(state, -1)
		self.visitedStates = [] 
		self.numLosses+=1
		if self.numLosses%100==0:
			print "Agent Memorize has ", self.numLosses, "losses"
	