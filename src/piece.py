import math

from importlib_metadata import pass_none


class Piece:
    def __init__(self , name , color , value , texture , texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self):
        pass

class Pawn(Piece):

    def __init__(self , color ):
        self.dir =-1 if color == 'white' else 1
        super().__init__('pawn' , color , 1.0)

class Knight(Piece):
    def __init__(self , color):
        super().__init__('knight' , color , 3.0)

class Bishop(Piece):
    def __init__(self , color):
        super().__init__('bishop' , color , 3.0)

class Rook(Piece):
    def __init__(self , color):
        super().__init__('rook' , color , 5.0)

class Queen(Piece):
    def __init__(self , color):
        super().__init__('Queen' , color , 9.0)

class King(Piece):
    def __init__(self , color):
        super().__init__('King' , color , math.inf)