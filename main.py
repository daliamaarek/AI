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
	visited = []
	nodes = Queue()
	setQueue(nodes, strategy)
	curr_state = problem.initial_state
	initial_node = Node()
	initial_node.state = curr_state
	initial_node.depth = 0
	nodes.enqueue(initial_node)
	final_depth = 0
	if(strategy == "ID"):
		while True:
			while len(nodes) > 0:
				curr_node = nodes.dequeue()
				if problem.goalTest(curr_node) : 
					return curr_node
				if(strategy == "ID" and curr_node.depth >= final_depth):
					continue
				children_size = len(curr_node.expand(problem.operators))
				children = curr_node.expand(problem.operators)
				for i in range(0, children_size):
					nodes.enqueue(children[i])
			final_depth = final_depth + 1
	else:
		while nodes.len() > 0 :
			nodes.dequeue()
			curr_node = nodes.dequeuedValue
			print "QUEUE SIZE: " + str(nodes.len())
			if(curr_node.state in visited):
				continue
			visited = visited + [curr_node.state]
			# print curr_node.cost
			print "Pokemons Captured: " + str(curr_node.state.pokemonCaptured)
			print "Curr Row: " + str(curr_node.state.row)
			print "Curr Col: " + str(curr_node.state.column)
			print "Depth " + str(curr_node.depth)
			print "Direction " + str(curr_node.state.direction)
			print "Path Cost " + str(curr_node.cost)
			if(curr_node.parent != None):
				print "Parent row" + str(curr_node.parent.state.row)
				print "Parent Col" + str(curr_node.parent.state.column)
			print "NODE DONE"

			if(strategy == "ID" and curr_node.depth > final_depth):
				continue
			if problem.goalTest(curr_node):
				print 'Found' 
				return curr_node
			children_size = len(curr_node.expand(problem.operators))
			children = curr_node.expand(problem.operators)
			for i in range(0, children_size):
				nodes.enqueue(children[i])
	return None

# def valid(row,column):
# 	return row >= 0 and row < maze.field.rows and column >= 0 and column < maze.field.columns

def setQueue(nodes, strategy):
	if strategy == "BF" :
		nodes.searchType = "FIFO"
	elif strategy == "DF":
		nodes.searchType = "LIFO"
	elif strategy == "ID":
		nodes.searchType = "LIFO"
	elif strategy == "UC":
		nodes.searchType = "PrioritizedInsert"

maze.genMaze()

print "Required Steps: " + str(maze.steps)
for i in range(0,rows):
	for j in range(0,columns):
		print field[i][j].walls


print "-------------------------------------"

print maze.map
print (1,0) in maze.map
print "NODES VISITED"


#GR and AS is missing
state = State()
state.row = 2
state.column = 2
state.direction = 3
pokemons_size = len(maze.map)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()

# <<<<<<< HEAD
# final_state.row = 1
# final_state.column = 1

# problem = Problem(["F","RL","RR"], state, final_state, 1, maze.steps)
# generalSearch(maze, "DF", False, problem.operators) 
# =======

final_state.row = 0
final_state.column = 0
final_state.pokemonCaptured = ""
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)
node = generalSearch(maze, "DF", False) 

print (node is None)

h = Heuristics()

print "-------------------------------------"
print "nearest pokemon"

n = Node()
n.state = state

print "shortest path " + str(h.manhattanPokemon(maze, n ))
print n.state.direction
print "-------------------------------------"

print "Pokemons"

for i in range(0,rows):
	for j in range(0,columns):
		if(field[i][j].isPokemon == True):
			print "(i,j) = " + str((i,j))



