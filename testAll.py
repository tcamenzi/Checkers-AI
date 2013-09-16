# from GUI import GUI 
from FakeGui import FakeGui
from HumanAgent import HumanAgent 
from Environment import Environment 
from RandomAgent import RandomAgent 
from time import sleep
import datetime, random
time = datetime.datetime.now


# Agent1 = HumanAgent(GUI, Environment, 'R')
Agent1 = RandomAgent(Environment, 'R')
Agent2 = RandomAgent(Environment, 'B')
# Agent2 = HumanAgent(GUI, Environment, 'B')


def playGame(agent1, agent2, environment, gui):
	state = environment.getStartState()
	gui.draw(state)

	# agent1PrevState = None
	# agent1NextState = None

	# agent2PrevState = None
	# agent2NextState = None

	while(True):
		move = agent1.nextMove(state)
		if move==None: #agent 1 has no available moves and has lost
			agent1.noteLoss()
			agent2.noteWin()
			break

		gui.highlightSquare(move[0][0], move[0][1])
		gui.highlightSquare(move[1][0], move[1][1])
		# sleep(.1)
		state = environment.updateState(state, move) 
		gui.draw(state)

		# agent1NextState = state 
		# agent1.learn(agent1PrevState, agent1NextState, 0)
		# agent1PrevState = agent1NextState 

		move = agent2.nextMove(state)
		if move==None:
			agent1.noteWin()
			agent2.noteLoss()
			break
		gui.highlightSquare(move[0][0], move[0][1])
		gui.highlightSquare(move[1][0], move[1][1])
		# sleep(.1)
		state = environment.updateState(state, move) 
		gui.draw(state)





		
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


