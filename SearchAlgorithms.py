from Cell import *
from Problem import *
from Maze import *
from Node import *
from State import *
from Queue import *
from createMaze import *
from searchVariables import *
from Heuristics import * 



def generalSearch(maze, strategy, visualize):

	# initialalize the start node
	initial_node = getInitialNode()

	# Initialize empty Queue and set its type according to
	# the search strategy
	nodes = initializeQueue(strategy, initial_node) 
	
	if(strategy == "ID"):
		final_depth = 0
		while True:
			nodes = initializeQueue(strategy, initial_node)
			return_node  = search(nodes, strategy, final_depth)
			if return_node is not None:
				return return_node
			final_depth  = final_depth + 1
	else:
		nodes.enqueue(initial_node)
		return_node = search(nodes,strategy)
		return return_node
	return None

def getInitialNode():
	# Get the initial state from the problem
	curr_state = problem.initial_state
	initial_node = Node()
	initial_node.state = curr_state
	initial_node.depth = 0
	initial_node = captureInitialPokemon(initial_node)
	return initial_node
def initializeQueue(strategy, initial_node):
	nodes = Queue()
	setQueue(nodes, strategy)
	nodes.enqueue(initial_node)
	return nodes

def captureInitialPokemon(initial_node):
	pokemonslist = list(initial_node.state.pokemonCaptured)
	if((initial_node.state.row,initial_node.state.column) in maze.map):
		pokemonslist[maze.map[(initial_node.state.row, initial_node.state.column)]] = '1'
	initial_node.state.pokemonCaptured = "".join(pokemonslist)
	return initial_node

def search(nodes,strategy, final_depth = 0):
	visited = []
	count_nodes = 0
	while nodes.len() > 0:
		count_nodes = count_nodes + 1
		nodes.dequeue()
		curr_node = nodes.dequeuedValue
		if((curr_node.state.pokemonCaptured, curr_node.state.direction, curr_node.state.row, curr_node.state.column, curr_node.cost, curr_node.state.steps) in visited):
			continue
		visited = visited + [(curr_node.state.pokemonCaptured, curr_node.state.direction, curr_node.state.row, curr_node.state.column, curr_node.cost, curr_node.state.steps)]
		if problem.goalTest(curr_node):
			return curr_node
		# curr_node.printNode()
		if(strategy == "ID" and curr_node.depth >= final_depth):
			continue
		children_size = len(curr_node.expand(problem.operators))
		children = curr_node.expand(problem.operators)
		for i in range(0, children_size):
			nodes.enqueue(children[i])
	return None

def bestFirstSearch(maze, evalFn, visualize):
	qnFunction = getHeuristic(evalFn)
	return generalSearch(maze, evalFn, visualize)

def Astar(maze, evalFn, visualize):
	qnFunction = getHeuristic(evalFn, 1)
	return generalSearch(maze, qnFunction, visualize)	

def getHeuristic(evalFn, a_star = None):
	heuristics = Heuristics(maze, final_state)
	if(evalFn == "H1"): #nearestPokemonManhattan
		if(a_star is not None):
			return heuristics.F1
		return heuristics.H1
	if(evalFn == "H2"): #goalPositionManhattan
		if(a_star is not None):
			return heuristics.F2
		return heuristics.H2
	if(evalFn == "H3"): #goalPositionManhattan
		if(a_star is not None):
			return heuristics.F3
		return heuristics.H3
	if(evalFn == "H4"): #numberOfPokemonsInDirection
		if(a_star is not None):
			return heuristics.F4
		return heuristics.H4

def setQueue(nodes, strategy):
	if strategy == "BF" :
		nodes.searchType = "FIFO"
	elif strategy == "DF":
		nodes.searchType = "LIFO"
	elif strategy == "ID":
		nodes.searchType = "LIFO"
	elif strategy == "UC":
		nodes.searchType = "PrioritizedInsert"
	else: 
		nodes.searchType = strategy