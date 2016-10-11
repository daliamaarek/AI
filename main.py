from Cell import *
from Problem import *
from Maze import *
from Node import *
from State import *
from Queue import *
from createMaze import *
from Heuristics import * 
from createMaze import *

def generalSearch(maze, strategy, visualize):
	# Initialize empty Queue and set its type according to
	# the search strategy
	nodes = Queue()
	setQueue(nodes, strategy)

	# Get the initial state from the problem
	curr_state = problem.initial_state

	# Initialize the start node
	initial_node = Node()
	initial_node.state = curr_state
	initial_node.depth = 0

	nodes.enqueue(initial_node)
	
	if(strategy == "ID"):
		final_depth = 0
		while True:
			nodes = Queue()
			setQueue(nodes, strategy)
			nodes.enqueue(initial_node)
			print "Iterative Deepening Depth: " + str(final_depth)
			return_node  = search(nodes, strategy, final_depth)
			if return_node is not None:
				return return_node
			final_depth  = final_depth + 1
	else:
		return_node = search(nodes,strategy)
		return return_node
	return None

def search(nodes,strategy, final_depth = 0):
	while nodes.len() > 0:
		nodes.dequeue()
		curr_node = nodes.dequeuedValue
		if problem.goalTest(curr_node):
			print 'Found'  
			return curr_node
		curr_node.printNode()
		if(strategy == "ID" and curr_node.depth >= final_depth):
			continue
		children_size = len(curr_node.expand(problem.operators))
		children = curr_node.expand(problem.operators)
		for i in range(0, children_size):
			nodes.enqueue(children[i])
	return None

def setQueue(nodes, strategy):
	if strategy == "BF" :
		nodes.searchType = "FIFO"
	elif strategy == "DF":
		nodes.searchType = "LIFO"
	elif strategy == "ID":
		nodes.searchType = "LIFO"
	elif strategy == "UC":
		nodes.searchType = "PrioritizedInsert"
#-----------------------------------------------------------------------

maze.genMaze()

print "Required Steps: " + str(maze.steps)
for i in range(0,rows):
	for j in range(0,columns):
		print field[i][j].walls
print "-------------------------------------"
print "NODES VISITED:"


#GR and AS is missing
state = State()
state.row = 1
state.column = 1
state.direction = 3
pokemons_size = len(maze.map)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()

final_state.row = 0
final_state.column = 0
final_state.pokemonCaptured = ""
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)
node = generalSearch(maze, "ID", False) 
if(node is not None):
	print "Final Node:"
	node.printNode()
print (node is None)
