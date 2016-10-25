from State import *
from Problem import *
from createMaze import *


def writeFacts(maze, directions):
	with open('KB.txt', 'w+') as kb:
		kb.write('Time(' + str(maze.steps) + ', Snode)\n')
		for i in range(0,maze.rows):
			for j in range(0,maze.columns):
				for k in range(0,len(maze.field[i][j].walls)):
					kb.write('wall(' + str(i) + ', ' + str(j) +', ' + str(maze.field[i][j].walls[k]) +')\n')
				if(maze.field[i][j].isPokemon):
					kb.write('Pokemon(' + str(i) + ', ' + str(j) + ', Snode)\n')
		kb.write('End(' + str(final_state.row) + ', ' + str(final_state.column) + ')\n')
		kb.write('Start(' + str(state.row) + ', ' + str(state.column) + ')\n')
		kb.write('Agent(' + str(state.row) + ', ' + str(state.column) + ', ' + directions[state.direction] + ', ' + 'Snode)\n')


# prim's algorithm
maze.genMaze()

#initial state
state = State()
state.row = 1
state.column = 1
state.direction = 3


pokemons_size = len(maze.map)
print 'size ' + str(pokemons_size)
# bitmask initially all zeros (no captured pokemons)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()
final_state.row = 0
final_state.column = 0
final_state.pokemonCaptured = ""

dd = ['UP', 'RIGHT', 'DOWN', 'LEFT']
writeFacts(maze, dd)
	
# goal state pokemon captured (all ones)
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

# initialize a problem with initial state and final state
problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)


