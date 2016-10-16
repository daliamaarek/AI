from State import *
from Problem import *
from createMaze import *

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

# goal state pokemon captured (all ones)
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

# initialize a problem with initial state and final state
problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)
