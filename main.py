from Cell import *
from Problem import *
from Maze import *
from Node import *
from State import *
from Queue import *

def generalSearch(maze, strategy, visualize):
	nodes = Queue()
	setQueue(nodes, strategy)
	curr_state = problem.initial_state
	initial_node = Node()
	initial_node.state = curr_state
	initial_node.depth = 0
	nodes.enqueue(initial_node)
	if(initial_node == None):
		print "MALAK"
	final_depth = 1
	max_depth = maze.rows * maze.columns * 100
	if(strategy == "ID"):
		while final_depth <= max_depth:
			while len(nodes) > 0 :
				curr_node = nodes.dequeue()
				if(strategy == "ID" and curr_node.depth > final_depth):
					continue
				if problem.goalTest(curr_node) : 
					return curr_node
				children_size = len(curr_node.expand())
				children = curr_node.expand()
				for i in range(0, children_size):
					nodes.enqueue(children[i])
			final_depth = final_depth + 1
	else:
		while nodes.len() > 0 :
			nodes.dequeue()
			curr_node = nodes.dequeuedValue
			# print curr_node.cost
			print curr_node.state.pokemonCaptured
			print curr_node.depth
			print curr_node.parent
			print "NODE DONE"

			if(strategy == "ID" and curr_node.depth > final_depth):
				continue
			if problem.goalTest(curr_node) : 
				return curr_node
			children_size = len(curr_node.expand())
			children = curr_node.expand()
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
		nodes.strategy = "PrioritizedInsert"


rows = 4
columns = 3
field = [[Cell() for j in range(columns)] for i in range(rows)]
for i in range(0,rows):
	for j in range(0,columns):
		field[i][j].row = i
		field[i][j].column = j



maze = Maze(field,rows,columns)
maze.genMaze()
for i in range(0,rows):
	for j in range(0,columns):
		print field[i][j].walls

print "-------------------------------------"

print "Pokemons"

for i in range(0,rows):
	for j in range(0,columns):
		if(field[i][j].isPokemon == True):
			print "(i,j) = " + str((i,j))
print "-------------------------------------"
print "NODES VISITED"
#GR and AS is missing
state = State()
state.row = 1
state.column = 1
state.direction = 0
pokemons_size = len(maze.map)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()
final_state.row = 3
final_state.column = 2

maze = Maze(field,rows,columns)
problem = Problem(["RR","RL","F"], state, final_state, 1, maze.steps)
generalSearch(maze, "BF", False)






