class Board:
    EMPTY_CELL = '.'

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.board = [[Board.EMPTY_CELL for c in range(cols)] for r in range(rows)]


    def set(self, col, row, value):
        if col < 0 or col >= self.cols or row < 0 or row >= self.rows:
            raise ValueError('Bad coords in set({},{}) call'.format(col, row))

        self.board[row][col] = value

    def drop(self, col, value):
        col_values = list(map(lambda r: r[col], self.board))
        index_of_highest_empty_cell = len(self.board)
        while True:
            if col_values[index_of_highest_empty_cell - 1] == Board.EMPTY_CELL:
                index_of_highest_empty_cell -= 1
                if index_of_highest_empty_cell == 0:
                    break
            else:
                break

        if index_of_highest_empty_cell < len(self.board):
            self.set(col, index_of_highest_empty_cell, value)
        else:
            raise ValueError('column {} is full'.format(col))

    def __str__(self):
        return '\n'.join(map(lambda r : ' '.join(map(str,r)), reversed(self.board)))

'''
b=Board(6,4)
b.set(1,0,'X')
print(b)
print()
b.drop(1,'X')
print(b)
print()
b.drop(1,'X')
print(b)
print()
b.drop(1,'X')
print()
print(b)
b.drop(1,'X')
print()
print(b)
'''