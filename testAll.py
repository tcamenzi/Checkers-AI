from GUI import GUI 
from FakeGui import FakeGui
from HumanAgent import HumanAgent 
from Environment import Environment 
from RandomAgent import RandomAgent 
from MemorizeStateAgent import MemorizeStateAgent
from MemorizeMonteCarlo import MemorizeMonteCarlo
from FeatureAgent import FeatureAgent
from time import sleep
import datetime, random, pickle
time = datetime.datetime.now


# Agent1 = HumanAgent(GUI, Environment, 'R')
Agent1 = FeatureAgent(Environment, 'R')
# Agent1 = MemorizeStateAgent(Environment, 'R')
# Agent1 = RandomAgent(Environment, 'R')
Agent2 = RandomAgent(Environment, 'B')
# Agent2 = HumanAgent(GUI, Environment, 'B')


def playGame(agent1, agent2, environment, gui, sleepTime):
	state = environment.getStartState()
	gui.draw(state)

	# agent1PrevState = None
	# agent1NextState = None

	# agent2PrevState = None
	# agent2NextState = None

	counter=0
	while(True):
		counter+=1
		print "round #",counter
		print "agent1 getting move"
		move = agent1.nextMove(state)
		if move==None: #agent 1 has no available moves and has lost
			print "NO MOVES FOR AGENT 1"
			agent1.noteLoss()
			agent2.noteWin()
			break
		print "agent 1 highlighting"
		gui.highlightSquare(move[0][0], move[0][1])
		gui.highlightSquare(move[1][0], move[1][1])
		print "agent 1 highlighting done"
		sleep(sleepTime)
		print "agent 1 environment updating state"
		state = environment.updateState(state, move) 
		print "agent 1 drawing state"
		gui.draw(state)

		# agent1NextState = state 
		# agent1.learn(agent1PrevState, agent1NextState, 0)
		# agent1PrevState = agent1NextState 

		print "agent2 getting move"
		move = agent2.nextMove(state)
		if move==None:
			print "NO MOVES FOR AGENT 2"
			agent1.noteWin()
			agent2.noteLoss()
			break
		print "agent 2 highlighting"
		gui.highlightSquare(move[0][0], move[0][1])
		gui.highlightSquare(move[1][0], move[1][1])
		print "agent 2 highlighting done"
		sleep(sleepTime)
		print "agent 2 environment updating state"
		state = environment.updateState(state, move) 
		print "agent 2 drawing state"
		gui.draw(state)

for i in range(100):
	playGame(Agent1, Agent2, Environment, FakeGui, 0)

print Agent1.numWins
print Agent1.numLosses
for feature in Agent1.featureWeights:
	print feature, Agent1.featureWeights[feature]

playGame(Agent1, Agent2, Environment, GUI, 1)
# for i in range(4000):
# 	playGame(Agent1, Agent2, Environment, FakeGui)


# print "Num wins: ", Agent1.numWins
# print "Num Losses: ", Agent1.numLosses


# f = open("data", 'wb')
# pickle.dump(Agent1.stateValueFxn, f)
# f.close()

# mymap =pickle.load(open('data', 'rb'))
# print "num elems in map: ", len(mymap)
# i=0
# for item in mymap:
# 	i+=1
# 	if mymap[item]!=1:
# 		for row in item:
# 			print row
# 		print mymap[item]
# 	if i>10:
# 		break


		
# def benchmark(method, *args):
# 	start = time()
# 	for i in range(10000):
# 		for item in method(*args):
# 			item=0
# 	end = time()
# 	print end-start

# playGame(Agent1, Agent2, Environment, GUI)
# print "start"
# for i in range(100):
# 	playGame(Agent1, Agent2, Environment, FakeGui)
# print "stop"

# def getRandomState():
# 	state = [ [0]*8 for i in range(8)]
# 	for i in range(8):
# 		for j in range(8):
# 			rint = random.randint(0,2)
# 			if rint==0:
# 				square = ''
# 			elif rint == 1:
# 				square = 'R'
# 			else:
# 				square='B'
# 			state[i][j] = square 
# 	return tuple(tuple(row) for row in state)

# state = Environment.getStartState()
# move = ( (0,0), (1,1))
# benchmark(Environment.getMoves, state, 'R')
# benchmark(Environment.updateState, state, move)

# start = time()
# for i in range(100000):
	
# 	for item in Environment.getJumpsForPiece(state,0,0,'R'):
# 		item=0
# 	for item in Environment.getJumpsForPiece(state,1,0,'R'):
# 		item=0
# end = time()
# print end-start


