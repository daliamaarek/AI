from State import *
from Problem import *
from createMaze import *
from subprocess import call

def writeFacts(maze, directions):
	with open('KB.txt', 'w+') as kb:
		kb.write(':- initialization main.\n')
		kb.write('rows(' + str(maze.rows) + ').\n')
		kb.write('cols(' + str(maze.columns) + ').\n')
		kb.write('totaltime(' + str(maze.steps) + ', snode).\n')
		kb.write('time(' + str(0) + ', snode).\n')
		for i in range(0,maze.rows):
			for j in range(0,maze.columns):
				for k in range(0,len(maze.field[i][j].walls)):
					kb.write('wall([' + str(i) + ', ' + str(j) +'], ' + str(maze.field[i][j].walls[k]).lower() +').\n')
		for i in range(0,maze.rows):
			for j in range(0,maze.columns):
				if(maze.field[i][j].isPokemon):
					kb.write('pokemon([' + str(i) + ', ' + str(j) + '], snode).\n')
		kb.write('end([' + str(final_state.row) + ', ' + str(final_state.column) + ']).\n')
		# kb.write('start([' + str(state.row) + ', ' + str(state.column) + ']).\n')
		kb.write('loc([' + str(state.row) + ', ' + str(state.column) + '], ' + directions[state.direction].lower() + ', ' + 'snode, _).\n')
		kb.close()	

	filenames = ['KB.txt', 'predicates_and_axioms.txt']
	with open('totalKB.pl', 'w+') as outfile:
		for currfile in filenames:
			with open(currfile) as infile:
				outfile.write(infile.read())
    	outfile.close()
	call(["swipl", "totalKB.pl"])


# prim's algorithm
maze.genMaze()

#initial state
state = State()
state.row = 1
state.column = 1
state.direction = 3


pokemons_size = len(maze.map)
# print 'size ' + str(pokemons_size)
# bitmask initially all zeros (no captured pokemons)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()
final_state.row = 0
final_state.column = 0
final_state.pokemonCaptured = ""
	
# goal state pokemon captured (all ones)
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

# initialize a problem with initial state and final state
problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)
