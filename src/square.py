
class Square:

    def __init__(self, row , col, piece = None ):
        self.row = row
        self.col = col
        self.piece = None

    def has_piece(self):
        return self.piece != None