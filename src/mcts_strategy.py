import random, math

class Tree:
	def __init__(self, root_state):
		self.root = Node(root_state, None)

class Node:
	def __init__(self, state, parent, action):
		self.state = state
		self.parent = parent
		self.action = action # [value, col]
		self.visits = 0
		self.score = 0

	def populate_board(self, board):
		moves = []
		node = self
		while node.action != None:
			moves.insert(0, node.action)

		for value, col in moves:
			board.drop(col, value)


def ucb(node):
	if node.visits == 0:
		return math.inf
	return node.score + 2 * (math.log(node.parent.visits) / node.visits) ** 0.5

def get_child_with_highest_ucb(node):
	max_ucb = -math.inf
	max_child = None
	for child in node.children:
		if ucb(child) > max_ucb:
			max_child = child 
	return max_child

def is_leaf(node):
	return node.children == None or len(node.children) == 0

def get_next_states(current_state):
	return []

def create_children(node):
	assert node.children == None
	node.children = []
	for next_state in get_next_states(node.state):
		node.children.append(Node(next_state, node))

def is_terminal(board):
	return len(get_next_states(node.state)) == 0

def get_terminal_value(node):
	pass	

def play_game_to_finish(node):
	pass

def get_board_for_state(state):
	COLS = 7
	ROWS = 6
	LINE_LEN = 4
	board = Board(COLS, ROWS, LINE_LEN)


def simulate_game(tree):
	current = tree.root
	nodes_to_update = [current]
	while not is_leaf(current):
		current = get_child_with_highest_ucb(current)
		nodes_to_update.append(current)

	game_result = None
	board = get_board_for_state(current.state)
	if is_terminal(board):
		game_result = get_terminal_value(current)

	else:
		new_children = create_children(current)
		next_move = new_children[0]
		nodes_to_update.append(next_move)

		game_result = play_game_to_finish(next_move)

	for node_to_update in nodes_to_update:
		node_to_update.visits += 1
		nodes_to_update.score += game_result



class MctsStrategy:
    def __init__(self):
    	self.rollout_limit = 10

    def move(self, board_view):
        current_state = board_view.to_id()
        tree = Tree(current_state)

        for i in range(self.rollout_limit):
        	simulate_game(tree)

        return tree.get_best_move()


    def update(self, result):
    	pass