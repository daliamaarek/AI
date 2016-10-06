
def manhattan (self, maze, node ):





def getPokemons(self, maze , start_row , start_column, end_row, end_column):
	pokemons = []
	for i in range(start_row, end_row):
		for j in range(start_column,end_column):
			if(maze.field[i][j].isPokemon == True):
				pokemons.append(str((i,j)))			
	return pokemons			



