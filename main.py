
# problem = Problem()

def generalSearch(maze, strategy, visualize):
	nodes = Queue()
	setQueue(nodes, strategy)
	curr_state = problem.initial_state
	initial_node = Node()
	initial_node.state(curr_state)
	initial_node.depth(0)
	nodes.enqueue(initial_node)

	final_depth = 1
	max_depth = maze.rows * maze.columns * 100
	while final_depth <= max_depth:
		while len(nodes) > 0 :
			curr_node = nodes.dequeue()
			if(strategy == "ID" and curr_node.depth > final_depth):
				continue
			if problem.goalTest() : 
				return curr_node
			children_size = len(curr_node.expand())
			children = curr_node.expand()
			for i in range(0, children_size):
				nodes.enqueue(children[i])
		final_depth++
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

#GR and AS is missing