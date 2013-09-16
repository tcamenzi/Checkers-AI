from GUI import GUI 
# raw_input('press enter to continue')
from HumanAgent import HumanAgent 
from Environment import Environment 

Agent1 = HumanAgent(GUI, Environment, 'R')
Agent2 = HumanAgent(GUI, Environment, 'B')


def playGame(agent1, agent2, environment, gui):
	state = environment.getStartState()
	gui.draw(state)
	while(True):
		move = agent1.nextMove(state)
		state = environment.updateState(state, move) 
		for row in state:
			print row
		gui.draw(state)

		move = agent2.nextMove(state)
		state = environment.updateState(state, move) 
		gui.draw(state)




playGame(Agent1, Agent2, Environment, GUI)
