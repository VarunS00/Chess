from constants import BLACK, WHITE

class Piece:
    def __init__(self, row, col, color, image=None):
        #Stores row, column, color, and image
        self.row = row
        self.col = col
        self.color = color
        self.image = image
        #Stores whether the piece has moved, used for castling and pawn movement
        self.has_moved = False
        #Stores piece name. Subclasses will override this with their own name
        self.name = 'piece'
    #Moves pieces to a new square
    def move(self, row, col):
        #Updates row and column, and sets has_moved to true
        self.row = row
        self.col = col
        self.has_moved = True
    #Draws the piece on the board
    def draw(self, win, square_size):
        #Checks for image, then draws it on the board at the correct location
        if self.image:
            win.blit(self.image, (self.col * square_size, self.row * square_size))
    #Creates a copy of the piece for move simulation and check detection
    def copy(self):
        #Gets the class of the piece
        cls = self.__class__
        #Creates the duplicate piece with the same attributes
        new_piece = cls(self.row, self.col, self.color, self.image)
        #Copies the has_moved attribute
        new_piece.has_moved = self.has_moved
        #Returns the new piece
        return new_piece
    #Returns legal moves, overridden by subclasses
    def get_moves(self, board):
        return []
    #Returns the opposite color, used for move validation and check detection
    def enemy(self):
        return BLACK if self.color == WHITE else WHITE