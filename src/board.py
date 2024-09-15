from const import *
from square import Square
from piece import *
from move import Move

class Board:

    def __init__(self):
        self.squares = [[0 , 0 , 0 , 0, 0 , 0 , 0 , 0]for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self , piece , row , col):
        # calculate all possible legal moves

        def pawn_move():
            # steps
            steps = 1 if piece.moved else 2

            #vertical moves
            start = row +piece.dir
            end = row + (piece.dir * ( 1 + steps))
            for possible_move_row in range(start , end , piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        #create initial and final move squares
                        initial = Square(row , col)
                        final = Square(possible_move_row , col)
                        #create a new move
                        move = Move(initial , final)
                        #append new move
                        piece.add_move(move)
                    #blocked
                    else: break
                #not in range
                else: break

            #diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1 , col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row , possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        #create initial and final move squares
                        initial = Square (row , col)
                        final = Square (possible_move_row , possible_move_col)
                        #create a new move
                        move = Move(initial , final)
                        #append new move
                        piece.add_move(move)

        def knight_moves():
            #8 possible moves
            possible_moves = [
                (row - 2, col - 1),
                (row + 2 , col + 1),
                (row - 1 , col - 2),
                (row + 1 , col + 2),
                (row - 1 , col + 2),
                (row + 1 , col - 2),
                (row + 2 , col - 1),
                (row - 2 , col + 1),
            ]
            for possible_move in possible_moves:
                possible_move_row , possible_move_col = possible_move

                if Square.in_range(possible_move_col , possible_move_row):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        #create squares of the new move
                        initial = Square(row , col)
                        final = Square(possible_move_row , possible_move_col)
                        #create new move
                        move = Move(initial , final)
                        #append new valid move
                        piece.add_move(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr , col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

            while True:
                if Square.in_range(possible_move_col , possible_move_row):
                    # create possible new move
                    initial = Square(row, col)
                    final = Square(possible_move_row , possible_move_col)
                    move = Move(initial , final)

                    #empty = continue looping
                    if self.squares[possible_move_row][possible_move_col].is_empty():
                        #append new move
                        piece.add_move(move)


                    #has enemy piece = add move + break
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        #append new move
                        piece.add_move(move)
                        break

                    #has team piece = break
                    if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                        break
                #not in range
                else: break

                #incrementing incrs
                possible_move_row = possible_move_row + row_incr
                possible_move_col = possible_move_row + col_incr


        if isinstance(piece , Pawn):
            pawn_move()

        elif isinstance(piece , Knight):
            knight_moves()

        elif isinstance(piece , Bishop):
            straightline_moves([
                (-1,1) ,  #up-right
                (-1 , -1) ,  #up-left
                (1 , 1) , #down-right
                (1 , -1), #down-left
            ])

        elif isinstance(piece, Rook):
            straightline_moves([
                (-1 , 0) , #up
                (0 , 1) ,#right
                (1 , 0) , #down
                (0 , -1), #left
            ])

        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1),  # up-right
                (-1, -1),  # up-left
                (1, 1),  # down-right
                (1, -1),  # down-left
                (-1, 0),  # up
                (0, 1),  # right
                (1, 0),  # down
                (0, -1)  # left
            ])

        elif isinstance(piece, King):
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
            row_pawn , row_other = (6,7) if color == 'white' else (1,0)

            # Pawns
            for col in range(COLS):
                self.squares[row_pawn][col] = Square(row_pawn , col , Pawn(color))

            # Knights
            self.squares[row_other][1] = Square(row_other , 1 , Knight(color))
            self.squares[row_other][6] = Square(row_other , 6 , Knight(color))

            # Bishops
            self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
            self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

            # Rooks
            self.squares[row_other][0] = Square(row_other, 0, Rook(color))
            self.squares[row_other][7] = Square(row_other, 7, Rook(color))

            # Queen
            self.squares[row_other][3] = Square(row_other, 3, Queen(color))

            # Bishops
            self.squares[row_other][4] = Square(row_other, 4, King(color))
