# connect4

## setup
    pip freeze > requirements.txt
    pip install -r requirements.txt
    source .venv/bin/activate

## tests
from root of project:

    ./test.sh

## MCTS
create new tree with current state S as its root

	while game count < max game count:
		set current node to root node of tree
		while current node is not leaf:
			set current node to be child with higest UCB
		
		create child nodes for current node
		select any child node
		play random game from selected child
		update child and all its parents (back to the root) with result of game

see https://github.com/suragnair/alpha-zero-general