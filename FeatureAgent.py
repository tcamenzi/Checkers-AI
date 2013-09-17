from Globals import *
import random
class FeatureAgent:
	def __init__(self, environment, color):
		self.environment = environment
		self.color = color
		self.featureWeights = self.getInitialFeatureWeights()
		self.lastState = None
		self.alpha = 1
		self.numMoves = 10
		self.numWins = 0
		self.numLosses=0
		self.explore = .1

	def getInitialFeatureWeights(self):
		fw = {} #feature weights

		fw['NumEnemySingles'] = 0
		fw['NumEnemyKings'] = 0
		fw['NumSelfSingles'] = 0
		fw['NumSelfKings'] = 0

		return fw 

	def nextMove(self, state):
		self.numMoves+=1
		self.alpha = 10 / (self.numMoves**.5)
		moves = [item for item in self.environment.getMoves(state, self.color)]
		random.shuffle(moves)
		if len(moves)==0: #you lost, no possible moves
			return None

		'''explore:
		- don't learn the prev state from exploration
		- do update the lastState so you learn it the next round.
		'''
		if random.random()<self.explore:
			# print 'exploring'
			rint = random.randint(0, len(moves)-1)
			move =  moves[rint]
			self.lastState = self.environment.updateState(state, move)
			return move 

		bestMove = moves[0]
		bestValue = self.getAfterValue(state, moves[0], self.color)
		for move in moves:
			currValue = self.getAfterValue(state, move, self.color)
			if currValue > bestValue:
				bestValue = currValue 
				bestMove = move 

		'''At this point we have bestMove calculated. However, calculate bestMove using
		the method below as well to make sure that both check out.'''
		bestAfterState = self.findBestAfterState(state, self.color, 2)
		assert(bestAfterState!=None)
		bestMoveOtherCalculation = None
		for move in moves:
			afterstate = self.environment.updateState(state, move)
			if afterstate==bestAfterState: #will be true for some move
				bestMoveOtherCalculation = move 
		#print "best move" , bestMove
		#print "best move other", bestMoveOtherCalculation
		bestValueOtherCalculation = self.getAfterValue(state, bestMoveOtherCalculation, self.color)
		# if bestValue!=bestValueOtherCalculation:
		# 	print "best value: ", bestValue
		# 	print "best value other: ", bestValueOtherCalculation
		#assert(bestValue=<bestValueOtherCalculation)
		#assert(bestMoveOtherCalculation == bestMove)

		if self.lastState!=None: #don't learn the first time
			self.learn(self.lastState, bestValueOtherCalculation) #the last state led to the curr value
		self.lastState = self.environment.updateState(state, bestMoveOtherCalculation) #new last state
		return bestMoveOtherCalculation
			
	def findBestAfterState(self, state, color, recursionDepth):
		if recursionDepth==0:
			return state 

		moves = [move for move in self.environment.getMoves(state, color)]
		if len(moves)==0: #no moves available; means color loses, so calling state is winning,
		   					#return that to the caller which should recognize the winning condition as a great state.
			return None   

		bestAfterState = self.environment.updateState(state, moves[0])
		bestValue = self.score(bestAfterState, color)
		for move in moves:
			immediateAfterState = self.environment.updateState(state, move)
			leafAfterState = self.findBestAfterState(immediateAfterState, opposing(color), recursionDepth-1)
			if leafAfterState == None: #opponent cannot move, you win!!
				return immediateAfterState 
			value = self.score(leafAfterState, color)
			if value > bestValue:
				bestValue = value
				bestAfterState = immediateAfterState 

		return bestAfterState 



	def getAfterValue(self, state, move, color):
		afterstate = self.environment.updateState(state, move)
		value = self.score(afterstate, color)
		return value 

	def score(self, afterstate, color):
		score = 0
		for feature in self.featureWeights:
			featureScore = self.getFeatureScore(feature, afterstate, color)
			weight = self.featureWeights[feature]
			weightedScore = featureScore * weight 
			score+=weightedScore
		return score 

	def getFeatureScore(self, feature, afterstate, color):
		if feature=='NumEnemySingles':
			return self.getNumSingles(afterstate, opposing(color))
		elif feature=='NumSelfSingles':
			return self.getNumSingles(afterstate, color)
		elif feature=='NumEnemyKings':
			return self.getNumKings(afterstate, opposing(color))
		elif feature=='NumSelfKings':
			return self.getNumKings(afterstate, color)
		else:
			assert(False) #error, not a recognized feature

	def getNumSingles(self, afterstate, color):
		MAX_NUM_SINGLES	= 12.0
		total=0
		for row in afterstate:
			for item in row:
				if color in item and 'K' not in item:
					total+=1
		return total/MAX_NUM_SINGLES

	def getNumKings(self, afterstate, color):
		MAX_NUM_KINGS = 12.0
		total=0
		for row in afterstate:
			for item in row:
				if color in item and 'K' in item:
					total+=1
		return total/MAX_NUM_KINGS

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

	#to be called only for your color
	def learn(self, state, realValue):
		prevValue = self.score(state, self.color)
		error = realValue - prevValue 
		coeff = error*self.alpha

		for feature in self.featureWeights:
			featureScore = self.getFeatureScore(feature, state, self.color)
			self.featureWeights[feature]+=coeff*featureScore 




