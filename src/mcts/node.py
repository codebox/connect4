class Node:
    def __init__(self, parent, action):
        self.parent = parent
        self.action = action # [player_id, col]
        self.visits = 0
        self.score = 0
        self.children = None

    def is_leaf(self):
        return self.children is None or self.is_terminal()

    def is_terminal(self):
        return self.children == []
