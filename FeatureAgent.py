from Globals import *

class FeatureAgent:
	def __init__(self, environment, color):
		self.environment = environment
		self.color = color
		self.featureWeights = self.getInitialFeatureWeights()
		self.lastState = None
		self.alpha = 0.05
		self.numWins = 0
		self.numLosses=0

	def getInitialFeatureWeights(self):
		fw = {} #feature weights

		fw['NumEnemySingles'] = 0
		fw['NumEnemyKings'] = 0
		fw['NumSelfSingles'] = 0
		fw['NumSelfKings'] = 0

		return fw 

	def nextMove(self, state):
		moves = [item for item in self.environment.getMoves(state, self.color)]
		if len(moves)==0: #you lost, no possible moves
			return None

		bestMove = moves[0]
		bestValue = self.getAfterValue(state, moves[0])
		for move in moves:
			currValue = self.getAfterValue(state, move)
			if currValue > bestValue:
				bestValue = currValue 
				bestMove = move 

		if self.lastState!=None: #don't learn the first time
			self.learn(self.lastState, bestValue) #the last state led to the curr value
		self.lastState = self.environment.updateState(state, bestMove) #new last state
		return bestMove 
			


	def getAfterValue(self, state, move):
		afterstate = self.environment.updateState(state, move)
		value = self.score(afterstate)
		return value 

	def score(self, afterstate):
		score = 0
		for feature in self.featureWeights:
			featureScore = self.getFeatureScore(feature, afterstate)
			weight = self.featureWeights[feature]
			weightedScore = featureScore * weight 
			score+=weightedScore
		return score 

	def getFeatureScore(self, feature, afterstate):
		if feature=='NumEnemySingles':
			return self.getNumSingles(afterstate, opposing(self.color))
		elif feature=='NumSelfSingles':
			return self.getNumSingles(afterstate, self.color)
		elif feature=='NumEnemyKings':
			return self.getNumKings(afterstate, opposing(self.color))
		elif feature=='NumSelfKings':
			return self.getNumKings(afterstate, self.color)
		else:
			assert(False) #error, not a recognized feature

	def getNumSingles(self, afterstate, color):
		total=0
		for row in afterstate:
			for item in row:
				if color in item and 'K' not in item:
					total+=1
		return total

	def getNumKings(self, afterstate, color):
		total=0
		for row in afterstate:
			for item in row:
				if color in item and 'K' in item:
					total+=1
		return total

	def logState(self):
		print "Wins: ", self.numWins
		print "Losses: ", self.numLosses
		print "Weights: "
		for feature in self.featureWeights:
			print feature, self.featureWeights[feature]

	def noteWin(self):
		self.learn(self.lastState, 1) #should be value 1
		self.lastState = None
		self.numWins+=1

		if (self.numWins + self.numLosses)%100==0:
			self.logState()
			

	def noteLoss(self):
		self.learn(self.lastState, -1) #should be value -1
		self.lastState = None 
		self.numLosses+=1

		if (self.numWins + self.numLosses)%100==0:
			self.logState()

	def learn(self, state, realValue):
		prevValue = self.score(state)
		error = realValue - prevValue 
		coeff = error*self.alpha

		for feature in self.featureWeights:
			featureScore = self.getFeatureScore(feature, state)
			self.featureWeights[feature]+=coeff*featureScore 




