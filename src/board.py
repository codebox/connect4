class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.board = [['.' for c in range(cols)] for r in range(rows)]

    def set(self, col, row, value):
        if col < 0 or col >= self.cols or row < 0 or row >= self.rows:
            raise ValueError('Bad coords in set({},{}) call'.format(col, row))

        self.board[self.rows-row-1][col] = value

    def __str__(self):
        return '\n'.join(map(lambda r : ' '.join(map(str,r)), self.board))

'''
b=Board(6,4)
b.set(0,0,'X')
b.set(1,1,'X')
b.set(5,3,'O')
print(b)
'''